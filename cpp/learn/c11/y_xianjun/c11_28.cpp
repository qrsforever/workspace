#include <iostream>

// 参数和返回类型相同
struct Cal1 {
    // error if remove const: const Cal1’ as ‘this’ argument of ‘int Cal1::operator()(int)’ discards qualifiers [-fpermissive]
    int operator()(int) const { std::cout << "Cal1: int int" << std::endl; return 0; }
    double operator()(double) const { std::cout << "Cal1: double double" << std::endl; return 0.1; }
};

template <class Obj>
class Test1 {
public:
    template <typename Arg>
    Arg operator()(Arg& a) const
    {
        return invoke(a);
    }
private:
    Obj invoke;
};

// 参数和返回类型不同
struct Cal2 {
    double operator()(int) const { std::cout << "Cal2: double int" << std::endl; return 99.1; }
    int operator()(double) const { std::cout << "Cal2: int double" << std::endl; return 1; }
};

template <class Obj>
class Test2 {
public:
    template <typename Arg>
    typename std::result_of<Obj(Arg)>::type operator()(Arg& a) const
    {
        return invoke(a);
    }
private:
    Obj invoke;
};

int main(int argc, char *argv[])
{
    int a = 10;
    double b = 99.9;
    Test1<Cal1> t1;
    std::cout << t1(a) << std::endl;
    std::cout << t1(b) << std::endl;

    Test2<Cal2> t2;
    std::cout << t2(a) << std::endl;
    std::cout << t2(b) << std::endl;

    Test2<Cal1> t3;
    std::cout << t3(a) << std::endl;
    std::cout << t3(b) << std::endl;

    return 0;
}
