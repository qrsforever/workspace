/***************************************************************************
 *  Thread.h -
 *
 *  Created: 2018-05-31 14:28:07
 *
 *  Copyright NotQRS
 ****************************************************************************/

#ifndef __THREAD_H__
#define __THREAD_H__

#include "Runnable.h"

#include <pthread.h>

#ifdef __cplusplus

namespace UTILS {

class Thread : public Runnable {
public:
    Thread();
    Thread(Runnable *r);
    ~Thread();

    void start();
    void join();

#ifdef DEBUG_THREAD
    void setName(const char* name);
#endif

    virtual void run() = 0;

    static Thread *currentThread();

private:
    void _init();

private:
#ifdef DEBUG_THREAD
    char mName[32];
#endif
    Runnable *mRunnable;
    pthread_t mID;
    pthread_mutex_t mMutex;

    static void *threadEntry(void *r);
};

} /* namespace UTILS */

#endif // __cplusplus

#endif /* __THREAD_H__ */
