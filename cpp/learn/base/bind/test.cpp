#include <iostream>
#include <functional>
#include <string>

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

class A {
public:
    int i_ = 0; // C++11允许非静态（non-static）数据成员在其声明处（在其所属类内部）进行初始化

    void output(int x, int y)
    {
        std::cout << x << "" << y << std::endl;
    }

    void output2(const std::string &x, const std::string &y, int state)
    {

    }


    int test1(int a) { return 10; }
    int test2(std::string b) { return 20; }

};

int test1(int a) { return 10; }
int test1(std::string b) { return 20; }


int main(int argc, char *argv[])
{
    g_currentRun = f1;
    {
        g_currentRun(); //f1()
    }

    std::function<int(int)> t1 = std::bind(test1, 10);
    // std::function<int(std::string)> t2 = std::bind(test1, "20");

    constexpr int flag = 1;

    g_currentRun = std::bind(f2, flag);
    {
        g_currentRun(); //f2(1)
    }

    A a;
    std::function<void(int, int)> fr = std::bind(&A::output, &a, std::placeholders::_1, std::placeholders::_2);

    std::function<void(const std::string&, const std::string&, int)> fr2 = 
        std::bind(&A::output2, &a, 
            std::placeholders::_1, std::placeholders::_2, std::placeholders::_3);

    // std::function<int(int)> t3 = std::bind(&A::test1, &a, 10);
    // std::function<int(std::string)> t4 = std::bind(&A::test2, &a, std::string("20"));

    return 0;
}
