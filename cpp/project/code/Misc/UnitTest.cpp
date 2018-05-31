/***************************************************************************
 *  UnitTest.cpp - Unit Test
 *
 *  Created: 2018-05-31 18:20:13
 *
 *  Copyright NotQRS
 ****************************************************************************/

#include "Thread.h"
#include "SysTime.h"
#include "RingBuffer.h"

#include <unistd.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>

using namespace UTILS;

static RingBuffer *gRingBuffer = 0;

class MyThread : public Thread {
public:
    MyThread() { }
    MyThread(Runnable *r) : Thread(r) { }
    ~MyThread() { }
    void run();
};

void MyThread::run()
{
    std::cout << "MyThread run" << std::endl;
    sleep(2);
    std::cout << "MyThread end" << std::endl;
}

class MyRunnable : public Runnable {
public:
    MyRunnable() {}
    ~MyRunnable(){}
    void run();
};

void MyRunnable::run()
{
    std::cout << "MyRunnable run" << std::endl;
    int len = 0;
    char tmp[64] = { 0 };
    uint8_t *bufPointer;
    uint32_t bufLength;
    const int fixSize = 8;
    for (int i = 0; i < 99; ++i) {
        int blockSize = 0;
        len = sprintf(tmp, "123456789A123456789A123456789A123456789A-%02d\n", i);
        char *ptr = tmp;
        do {
            gRingBuffer->getWriteHead(&bufPointer, &bufLength);
            printf("------> Write length[%d] Content len[%d]\n", bufLength, len);
            if (bufLength > (len+fixSize+fixSize+3)) {
                snprintf(((char*)bufPointer+fixSize), len, "%s", ptr); 
                *((int *)(bufPointer+4)) = len;
                blockSize = (len+fixSize+fixSize+3) & 0xfffffffc;
                *((int *)(bufPointer+0)) = blockSize;
                gRingBuffer->submitWrite(bufPointer, blockSize);
                len = 0;
            } else if (bufLength > fixSize){
                printf("Warn: bufLength[%d] < (len[%d] + fixSize[%d])\n", bufLength, len, fixSize);
                memcpy((bufPointer+fixSize), ptr, (bufLength-fixSize));
                *((int *)(bufPointer+0)) = bufLength;
                *((int *)(bufPointer+4)) = bufLength - fixSize;
                gRingBuffer->submitWrite(bufPointer, bufLength);

                len -= (bufLength-fixSize); /* left length */
                ptr += (bufLength-fixSize);
            } else {
                printf("Warn: wait bufLength[%d]\n", bufLength);
                usleep(20*1000);
            }
        } while (len > 0);
    }
    std::cout << "MyRunnable end" << std::endl;
}

void test_Thread()
{
    std::cout << "test_Thread: " << std::endl;
    MyThread *myThread = new MyThread();
    std::cout << "test_Thread: start thread" << std::endl;
    sleep(1);
    myThread->start();
    std::cout << "test_Thread: sleep 1" << std::endl;
    sleep(1);
    myThread->join();
    std::cout << "test_Thread: end!" << std::endl;
}

void test_SysTime()
{
    SysTime::DateTime dt;
    SysTime::GetDateTime(&dt);
    printf("%04d/%02d/%02d %02d:%02d:%02d\n", 
        dt.mYear, dt.mMonth, dt.mDay, 
        dt.mHour, dt.mMinute, dt.mSecond);
    std::cout << "Clock ms time: " << SysTime::GetMSecs() << std::endl;
}

void test_RingBuffer()
{
    uint8_t *buf = (uint8_t*)malloc(128);
    gRingBuffer = new RingBuffer(buf, 128);
    MyRunnable *myRunnable = new MyRunnable();
    MyThread *myThread = new MyThread(myRunnable);
    myThread->start();

    uint8_t *bufPointer;
    uint32_t bufLength;
    const int fixSize = 8;
    char tmp[64] = { 0 };
    char rcv[64] = { 0 };
    for (int i = 0; i < 99; ++i) {
        while (1) {
            usleep(20*1000);
            gRingBuffer->getReadHead(&bufPointer, &bufLength);
            printf("##### Read : %d\n", bufLength);
            if (bufLength == 0)
                break;
            int blockSize = *((int *)(bufPointer + 0));
            int dataSize = *((int *)(bufPointer + 4));
            if (dataSize < sizeof(rcv)) {
                memcpy(rcv, (bufPointer + fixSize), dataSize);
                rcv[dataSize] = '\0';
                printf("%s", rcv);
            }
            printf("####read submit### %d\n", blockSize);
            gRingBuffer->submitRead(bufPointer, blockSize);
        }
    }
    std::cout << "test_RingBuffer end" << std::endl;
}

int main(int argc, char *argv[])
{
    // test_SysTime();
    // test_Thread();
    test_RingBuffer();
    
    return sleep(1000);
}
