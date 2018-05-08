#include <iostream>
#include <functional>

// constexpr：告诉编译器我可以是编译期间可知的，尽情的优化我吧。
// const：告诉程序员没人动得了我，放心的把我传出去；或者放心的把变量交给我，我啥也不动就瞅瞅。

// bind可以把带有参数的函数, 先绑定值, 函数参数就可变个数

typedef std::function<void()> Run;

Run g_currentRun;

void f1()
{
    std::cout << "f1()\n";
}

void f2(int flag)
{
    std::cout << "f2(" << flag << ")\n";
}

int main(int argc, char *argv[])
{
    g_currentRun = f1;
    {
        g_currentRun(); //f1()
    }

    constexpr int flag = 1;

    g_currentRun = std::bind(f2, flag);
    {
        g_currentRun(); //f2(1)
    }
    return 0;
}
