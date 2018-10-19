#include <iostream>
#include <map>
#include <limits>
#include <typeinfo>

using namespace std;

/* 简化程序 */
void test_simple()
{
    map< int, map<int,int> > m;
    // C++98/03 style:
    map<int, map<int,int> >::const_iterator it1 = m.begin();
    // C++11 style
    const auto it2 = m.begin();
}

/* 解决不了精度推到*/
void test_overflow()
{
    auto a = numeric_limits<unsigned int>::max();
    auto b = 1;
    auto c = a + b;// c is also unsigned int, and it is 0 since it has overfl
    cout << "c = " << c << endl;
}

void test_typeid()
{
    int tempA = 10;
    const int tempB = 10;

    auto &tempC = tempA;

    /* why? both is i */
    cout << "tempC = " << typeid(tempC).name() << endl;
    cout << "tempB = " << typeid(tempB).name() << endl;
}

// template<typename T1, typename T2>
// void sum(T1 &t1, T2 &t2, decltype(t1 + t2) &s)
// {
//     cout << "decltype(t1 + t2)  = " << typeid(decltype(t1 + t2)).name() << endl;
//     s = t1 + t2;
// }

// or (使用右值)

template<typename T1, typename T2>
void sum(T1 &&t1, T2 &&t2, decltype(t1 + t2) &s)
{
    cout << "1. decltype(t1 + t2)  = " << typeid(decltype(t1 + t2)).name() << endl;
    s = t1 + t2;
}

// or

template<typename T1, typename T2>
auto sum(T1 &t1, T2 &t2) -> decltype(t1 + t2)
{
    cout << "2. decltype(t1 + t2)  = " << typeid(decltype(t1 + t2)).name() << endl;
    return t1 + t2;
}

void test_sum()
{
    float s;
    float t1 = 10.0f, t2 = 10.0f;
    // sum(t1, t2, s);
    sum(1.0f, 1.0f, s); /* 使用右值 */
    cout << "s1 = " << s << endl;
    cout << "s2 = " << sum(t1, t2) << endl;
}

struct Default { int foo() const { return 1; } };

struct NonDefault
{
    NonDefault(const NonDefault&) { }
    int foo() const { return 1; }
};

// 专门对付没有默认构造函数的
void test_declval()
{
    decltype(Default().foo()) n1 = 1;                   // type of n1 is int
    //  decltype(NonDefault().foo()) n2 = n1;               // error: no default constructor
    decltype(declval<NonDefault>().foo()) n2 = n1; // type of n2 is int
    cout << "n1 = " << n1 << '\n'
        << "n2 = " << n2 << '\n';
}

/* result_of, c++17使用invoke_result instead */

template <typename F, typename Arg>
typename result_of<F(Arg)>::type
invoke(F f, Arg a)
{
    return f(a);
}

template <typename F, typename... Args>
typename result_of<F(Args...)>::type
invoke1(F f, Args...)
{
    return f(0.9);
}

// or

template <typename F, typename Arg>
auto invoke(F f, Arg a, Arg b) -> decltype(f(a, b)) //uses the f parameter
{
    return f(a, b);
}

// or

template <typename F, typename Arg>
auto invoke2(F f, Arg a) -> decltype(F()(a)) //"constructs" an F
{
    return f(a);
}

typedef double (*Func)(double);

double func(double d)
{
    return d;
}

long func1(int a, int b)
{
    return a + b;
}

void test_invoke()
{
    typename result_of<Func(double)>::type d = func(0.9);
    cout << "d = " << d << endl;

    double d1 = invoke(func, 0.34);
    cout << "d1 = " << d1 << endl;
}

int main(int argc, char *argv[])
{
    test_simple();
    test_overflow();
    test_typeid();
    test_sum();
    test_declval();
    test_invoke();
    return 0;
}
