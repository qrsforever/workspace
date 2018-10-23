#include <iostream>

template <typename...T>
struct Count {
};

template <>
struct Count<> {
    static const int value = 0;
};

template<typename T, typename... Args>
struct Count<T, Args...>
{
    static const int value = 1 + Count<Args...>::value;
};

template<typename... Args>
struct Count2
{
    static const int value = sizeof...(Args);
};

int main(int argc, char *argv[])
{
    std::cout << "args: " << Count<int,short,char>::value << std::endl;
    std::cout << "args: " << Count<int,short,char>().value << std::endl;
    std::cout << "args: " << Count2<int,char>::value << std::endl;
    return 0;
}
