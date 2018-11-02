#include <iostream>
#include <string>

template<typename A1, typename A2, int>
class SomeType
{
public:
    void f(A1 a1, A2 a2) {
        std::cout << "a1 = " << a1 << " a2 = " << a2 << std::endl;
    }
};

template<typename A2>
using TypedefName = SomeType<float, A2, 10>;

using Func_t = void(*)(int);

using Func2_t = std::string(*)(int);

void test(int a)
{
    return;
}

std::string test2(int a)
{
    return "hello";
}

int main(int argc, char *argv[])
{
    Func_t f = test;
    TypedefName<char> tn;
    tn.f(1.1, 'a');

    Func2_t f2 = test2;
    std::cout << "--> " << f2(1) << std::endl;
    return 0;
}
