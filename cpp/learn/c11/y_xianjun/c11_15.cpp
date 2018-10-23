#include <iostream>

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

void test(int a)
{
    return;
}

int main(int argc, char *argv[])
{
    Func_t f = test;
    TypedefName<char> tn;
    tn.f(1.1, 'a');
    return 0;
}
