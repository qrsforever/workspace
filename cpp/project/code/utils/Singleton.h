#ifndef _QRS_SINGLETON_H_
#define _QRS_SINGLETON_H_

#include "Mutex.h"

namespace QRS {

template<typename TYPE>
class Singleton {
public:
    static TYPE& getInstance(){
        Mutex::Autolock _l(_sLock);
        TYPE* instance = _sInstance;
        if (0 == instance) {
            instance = new TYPE();
            _sInstance = instance;
        }
        return *instance;
    }
protected:
    Singleton() {}
    ~Singleton() {}

private:
    Singleton(const Singleton&);
    Singleton& operator= (const Singleton&);
    static TYPE* _sInstance;
    static Mutex _sLock;
};

#define QRS_SINGLETON_STATIC_INSTANCE(TYPE)                 \
    template<> Mutex Singleton< TYPE >::_sLock(Mutex::PRIVATE);  \
    template<> TYPE* Singleton< TYPE >::_sInstance(0);           \
    template class Singleton< TYPE >;

}

#endif /* ifndef _LEECO_SINGLETON_H */
