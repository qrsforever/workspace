#ifndef __LOOPERJNI_DEMO_H
#define __LOOPERJNI_DEMO_H

#include <utils/Thread.h>
#include <utils/Looper.h>
#include <sys/types.h>

namespace android {

class MyHandlerThread : public Thread {
public:
    explicit MyHandlerThread();
    ~MyHandlerThread();
    void onFirstRef();
    void onLastStrongRef(const void* id);

    sp<Looper> getLooper();
    status_t readyToRun();
    bool isOk() { return bOk; }
private:
    virtual bool threadLoop();

    sp<Looper> mLooper;
    bool bOk;
};

class MyMessageHandler : public MessageHandler {
public:
    MyMessageHandler(sp<Looper> looper);
    ~MyMessageHandler();
    virtual void handleMessage(const Message& message);
    void sendEmptyMessage(int what);
    void sendEmptyMessageDelay(int msec, int what);
private:
    sp<Looper> mLooper;
};

class MyLooperCallback : public LooperCallback {
protected:
    virtual ~MyLooperCallback();

public:
    MyLooperCallback();
    virtual int handleEvent(int fd, int events, void* data);
};

}

#endif
