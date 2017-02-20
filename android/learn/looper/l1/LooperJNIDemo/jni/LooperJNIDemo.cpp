#include "LooperJNIDemo.h"
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/socket.h>

#define CMD_LOG 1
#define CMD_DELAY_LOG 2

namespace android {

MyHandlerThread::MyHandlerThread() 
    : Thread(false)
    , mLooper(0), bOk(false)
{
}

MyHandlerThread::~MyHandlerThread()
{
}

status_t 
MyHandlerThread::readyToRun() // 线程启动第一次loop时调用
{
    printf("MyHandlerThread readyToRun\n");
    mLooper = Looper::prepare(0);
    bOk = true;
    return 0;
}

sp<Looper> 
MyHandlerThread::getLooper()
{
    return mLooper;
}

void 
MyHandlerThread::onFirstRef() // BaseRef调试接口
{
    printf("MyHandlerThread onFirstRef\n");
}

void 
MyHandlerThread::onLastStrongRef(const void* id) // BaseRef调试接口
{
    printf("MyHandlerThread onLastStrongRef pointer: %p\n", id);
}

bool 
MyHandlerThread::threadLoop()
{
    printf("MyHandler threadid: %d\n",  getTid());
    if (mLooper != 0)
        mLooper->pollOnce(-1); // -1: epoll有事件才触发, 0: epoll立即返回, >0: 超时时间返回
    // sp<Looper> looper = Looper::getForThread();
    // if (looper != 0)
        // looper->pollOnce(1000);
    return true; // 返回true, 循环loop, 否则退出loop
}

MyMessageHandler::MyMessageHandler(sp<Looper> looper) 
    : mLooper(looper) 
{
}

MyMessageHandler::~MyMessageHandler()
{
}

void
MyMessageHandler::handleMessage(const Message& message)
{
    switch (message.what) {
        case CMD_LOG:
            printf("MyMessageHandler handleMessage exec CMD_LOG\n");
            break;
        case CMD_DELAY_LOG:
            printf("MyMessageHandler handleMessage exec CMD_DELAY_LOG\n");
            break;
        default:
            break;
    }
}

void 
MyMessageHandler::sendEmptyMessage(int what)
{
    Message message(what);
    mLooper->sendMessage(this, message);
}

void 
MyMessageHandler::sendEmptyMessageDelay(int msec, int what)
{
    Message message(what);
    mLooper->sendMessageDelayed(msec * 1000000 /*ns*/, this, message);
}

MyLooperCallback::MyLooperCallback()
{
}

MyLooperCallback::~MyLooperCallback()
{
}

int 
MyLooperCallback::handleEvent(int fd, int events, void* data)
{
    if (events & ALOOPER_EVENT_INPUT) {
        char buff[16] = { 0 };
        ssize_t nRead;
        do {
            nRead = ::recv(fd, (void*)buff, sizeof(buff), MSG_DONTWAIT);
        } while (nRead == -1 && errno == EINTR);
        printf("MyLooperCallback::handleEvent: %s\n", buff);
    }
    return 1; // 返回1 继续监听该fd, 否则删除fd
}

}

#define SOCKET_BUFFER_SIZE 32 * 1024
using namespace android;
int main(int argc, char const* argv[])
{
    // MyHandlerThread* thread = new MyHandlerThread(); // 这种方法是错误的
    sp<MyHandlerThread> thread = new MyHandlerThread(); 
    printf("main threadid: %d\n", gettid());
    thread->run();
    while (!thread->isOk()) {
        sleep(1);
    }
    sp<Looper> looper = thread->getLooper();


    sp<MyMessageHandler> handler = new MyMessageHandler(looper);
    for (int i = 0; i < 5; ++i) {
        if (i%2) {
            handler->sendEmptyMessage(CMD_LOG);
            continue;
        }
        sleep(1);
        handler->sendEmptyMessageDelay(10000, CMD_DELAY_LOG);
    }

    int sockets[2];
    int bufferSize = SOCKET_BUFFER_SIZE;
    if (socketpair(AF_UNIX, SOCK_SEQPACKET, 0, sockets)) {
        printf("main ocketpair error!\n");
        goto END;
    }
    setsockopt(sockets[0], SOL_SOCKET, SO_SNDBUF, &bufferSize, sizeof(bufferSize));
    setsockopt(sockets[0], SOL_SOCKET, SO_RCVBUF, &bufferSize, sizeof(bufferSize));
    setsockopt(sockets[1], SOL_SOCKET, SO_SNDBUF, &bufferSize, sizeof(bufferSize));
    setsockopt(sockets[1], SOL_SOCKET, SO_RCVBUF, &bufferSize, sizeof(bufferSize));
    fcntl(sockets[0], F_SETFL, O_NONBLOCK);
    fcntl(sockets[1], F_SETFL, O_NONBLOCK);
    looper->addFd(sockets[1], ALOOPER_POLL_CALLBACK, ALOOPER_EVENT_INPUT, new MyLooperCallback(), 0);
    for (int i = 0; i < 5; ++i) {
        char buff[16] = { 0 };
        sprintf(buff, "%s-%d", "Test", i);
        ssize_t nWrite;
        do {
            nWrite = ::send(sockets[0], buff, sizeof(buff), MSG_DONTWAIT | MSG_NOSIGNAL);
        } while (nWrite == -1 && errno == EINTR);
        sleep(1);
    }

END:
    return sleep(100);
}



