#ifndef _COMMON_MUTEX_H_
#define _COMMON_MUTEX_H_

#include <pthread.h>

namespace QRS {

class Mutex {
public:
    enum {  
        PRIVATE = 0,
        SHARED = 1,
    };
    Mutex();
    Mutex(const char* name);
    Mutex(int type, const char* name = 0);
    ~Mutex();
    int lock();
    void unlock();
    int trylock();

    class Autolock {
    public:
        inline Autolock(Mutex& mutex) : _mLock(mutex) { _mLock.lock(); } 
        inline Autolock(Mutex* mutex) : _mLock(*mutex) { _mLock.lock(); } 
        inline ~Autolock() { _mLock.unlock(); }
    private:
        Mutex& _mLock;
    };

private:
    // cannot be copied
    Mutex(const Mutex&);
    Mutex& operator = (const Mutex&);
    pthread_mutex_t _mMutex;
};

inline Mutex::Mutex() 
{
    pthread_mutex_init(&_mMutex, 0);
}

inline Mutex::Mutex(__attribute__((unused)) const char* name) 
{
    pthread_mutex_init(&_mMutex, 0);
}

inline Mutex::Mutex(int type, __attribute__((unused)) const char* name)
{
    if (type == SHARED) {
      pthread_mutexattr_t attr; 
      pthread_mutexattr_init(&attr);
      pthread_mutexattr_setpshared(&attr, PTHREAD_PROCESS_SHARED);
      pthread_mutex_init(&_mMutex, &attr);
      pthread_mutexattr_destroy(&attr);
    } else {
      pthread_mutex_init(&_mMutex, 0);
    }
}

inline Mutex::~Mutex()
{
    pthread_mutex_destroy(&_mMutex);
}

inline int Mutex::lock()
{
    return -pthread_mutex_lock(&_mMutex);
}

inline void Mutex::unlock()
{
    pthread_mutex_unlock(&_mMutex);
}

inline int Mutex::trylock()
{
    return -pthread_mutex_trylock(&_mMutex);
}

typedef Mutex::Autolock AutoMutex;

} 

#endif
