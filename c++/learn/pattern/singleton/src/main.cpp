#include "utils/Singleton.h"
#include <iostream>

namespace QRS {

class LeecoSingleton : public Singleton<LeecoSingleton> {
public:
    LeecoSingleton() { }
    ~LeecoSingleton() { }
    void call() { std::cout << "Hello world" << std::endl; }

    // friend class Singleton<LeecoSingleton>;
private:

};

QRS_SINGLETON_STATIC_INSTANCE(LeecoSingleton)

}

int main(int argc, char *argv[])
{
    QRS::LeecoSingleton::getInstance().call(); 
    return 0;
}
