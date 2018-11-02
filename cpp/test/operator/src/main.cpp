#include <iostream>
#include <functional>

auto a = (10);

// 下面两行有什么不同吗
std::function<int(int)> f1 = ([](int a) { return a; });
std::function<int(int)> f2 = [](int a) { return a; };

class Test {
public:
    Test() {}
    ~Test() {}
    int operator() (int arg) { return 99; }
    void func() {
        int t = (10);
        std::cout << t << std::endl;
    }
};

int main(int argc, char *argv[])
{
    Test t;
    std::cout << t(11) << std::endl;
    t.func();
    std::cout << f1(1) << std::endl;
    std::cout << f2(2) << std::endl;
    return 0;
}
