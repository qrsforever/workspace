/***************************************************************************
 *  test.cpp - test
 *
 *  Created: 2018-06-05 18:32:39
 *
 *  Copyright QRS
 ****************************************************************************/

#include <stdexcept>
#include <functional>
#include <memory>
#include <cstdio>
#include <map>

template<typename R, typename... Args>
class Functor {
public:
    Functor(std::function<R(Args...)> fun) : _fun(fun) {

    }

    template<typename Object>
    Functor(Object* object, R (Object::*method)(Args...))
        : _fun([object, method](Args... args){ return (*object.*method)(args...);}) {

    }

    R operator()(Args... args) {
        return _fun(args...);
    }
private:
    std::function<R(Args...) > _fun;
};

template <typename T_return> inline char get_return_code() {
    throw std::logic_error("test: Adding function with invalid return type");
}
template <> inline char get_return_code<void>() { return 'v'; }
template <> inline char get_return_code<int>()  { return 'i'; }
template <> inline char get_return_code<std::string>() { return 's'; }

template <typename T_return> inline char get_argument_code() {
    throw std::logic_error("test: Adding function with invalid argument type");
}
template <> inline char get_argument_code<int>() { return 'i'; }
template <> inline char get_argument_code<char>() { return 'c'; }
template <> inline char get_argument_code<std::string>() { return 's'; }

void* gCB = 0;

// std::map<std::string, auto> gFuns;

template < typename T_return >
bool add_function(std::string name, Functor<T_return> *call)
{
    printf("name[%s], get_return_code[%c]\n", name.c_str(), get_return_code<T_return>());
    (*call)();
    return true;
}

template < typename T_return, typename T_arg1 >
bool add_function(std::string name, Functor<T_return, T_arg1> *call)
{
    printf("name[%s], get_return_code[%c] get_argument_code[%c]\n",
        name.c_str(),
        get_return_code<T_return>(),
        get_argument_code<T_arg1>()
        );
    // call(100);
    gCB = (void*)call;
    return true;
}

template < typename T_return, typename T_arg1, typename T_arg2>
bool add_function(std::string name, std::shared_ptr<Functor<T_return, T_arg1, T_arg2>> call)
{
    printf("name[%s], get_return_code[%c] arg1[%c] arg2[%c]\n", name.c_str(),
        get_return_code<T_return>(),
        get_argument_code<T_arg1>(),
        get_argument_code<T_arg2>());

    printf("call count[%d]\n", call.use_count());

    printf("\t call(100, 'x') = %d\n", (*call)(100, 'x'));
    return true;
}

int test1()
{
    printf("test1 return\n");
    return 0;
}

void test2(int a)
{
    printf("test2 a[%d]\n", a);
}

int test3(int a, char b)
{
    printf("test3 a[%d] b[%c]\n", a, b);
    return 989;
}

class Test {
public:
    Test() {}
    ~Test() {}
    std::string test4(int a) {
        printf("test4 a[%d]\n", a);
        return "helloworld";
    }
};

int main(void)
{
    /*
     * 测试模板
     * */
    add_function("test1", new Functor<int>(test1));
    add_function("test2", new Functor<void, int>(test2));

    /*
     * 测试类型转换
     * */
    Functor<void, int> call = *(static_cast<Functor<void, int>*>(gCB));
    call(100);

    /*
     * 测试智能指针
     */
    add_function("test3", std::make_shared<Functor<int, int, char>>(test3));

    /*
     * 测试使用对象中的方法
     */
    Test *t = new Test();
    add_function("test4", new Functor<std::string, int>(t, &Test::test4));
    return 0;
}
