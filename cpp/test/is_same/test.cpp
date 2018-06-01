#include <iostream>

struct true_type
{
    enum __value__ {value = true};
};

struct false_type
{
    enum __value__ {value = false};
};

template<typename T, typename U>
struct is_same : false_type {};

template<typename T>
struct is_same<T, T> : true_type {};

template<typename T>
bool f_is_same(T, T)
{
    return true;
}

template<typename T, typename U>
bool f_is_same(T, U)
{
    return false;
}

class A {
public:
    A() { }
    ~A() { }
};

class B : public A {
public:
    B() { }
    ~B() { }
};

int main(int argc, char *argv[])
{
    // int a = 10;
    // std::cout << is_same<a, int>::value  << std::endl;
    std::cout << is_same<int, int>::value  << std::endl;
    std::cout << is_same<int, char>::value  << std::endl;

    std::cout << f_is_same(new int(), new int()) << std::endl;
    std::cout << f_is_same(new int(), new char()) << std::endl;
    return 0;
}
