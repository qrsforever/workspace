/***************************************************************************
 *  test.cpp - test
 *
 *  Created: 2018-06-05 18:32:39
 *
 *  Copyright QRS
 ****************************************************************************/

#include <stdexcept>
#include <functional>
#include <cstdio>

template<typename R = void, typename... Args>
class Functor {
public:
    Functor(std::function<R(Args...)> fun) : _fun(fun) {

    }

    R operator()(Args... args) {
        return _fun(args...);
    }
private:
    std::function<R(Args...) > _fun;
};

template <typename T_return> inline char get_return_code() {
    throw std::logic_error("clipsmm: Adding function with invalid return type");
}
template <> inline char get_return_code<void>() { return 'v'; }
template <> inline char get_return_code<int>()  { return 'i'; }

template <typename T_return> inline char get_argument_code() {
    throw std::logic_error("clipsmm: Adding function with invalid argument type");
}
template <> inline char get_argument_code<int>() { return 'i'; }
template <> inline char get_argument_code<std::string>() { return 's'; }

void* gCB = 0;

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

int test1()
{
    printf("test1 return\n");
    return 0;
}

void test2(int a)
{
    printf("test2 a[%d]\n", a);
}

int main(void)
{
    add_function("test1", new Functor<int>(test1));
    add_function("test2", new Functor<void, int>(test2));

    Functor<void, int> call = *(static_cast<Functor<void, int>*>(gCB));
    call(100);

    return 0;
}
