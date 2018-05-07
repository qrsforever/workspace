#include <iostream>
#include <utility>

// https://blog.csdn.net/viggirl/article/details/52858108

// 并不移动什么
// std::move的作用只是为了让调用构造函数的时候告诉编译器去选择移动构造函数.
//

// 右值引用是C++11中最重要的新特性之一，它解决了C++中大量的历史遗留问题，
// 使C++标准库的实现在多种场景下消除了不必要的额外开销（如std::vector, std::string)，
// 也使得另外一些标准库（如std::unique_ptr, std::function）成为可能。即使你并不直接使用右值引用，
// 也可以通过标准库，间接从这一新特性中受益。
// 为了更好的理解标准库结合右值引用带来的优化，我们有必要了解一下右值引用的重大意义。
// 

// lvalue和rvalue的前缀怎么理解，left和right？好吧，l表示location，r表示read。
// location表示可以在内存中寻址，可以被赋值，read表示可以直接知道值 
// std::move()来将左值转换成右值引用

// && 和 &一样都是引用，&&是新标准弄出来的，称为 右值引用。

// 无名右值引用
// 一般由static_cast < T&& >(t)转换操作转换而来
// 也可以用标准库提供的std::move()来将左值转换成右值引用
//
// 带名右值引用
// T&& 这是一个左值，只不过她的类型是右值引用，只能绑定右值
// 额外说一句：如果类型是T&& 且这个T类型无需推导即可确定，那么这个变量称为带名右值引用；如果这个T类型需要推导，那么这个变量称为转发型引用。
// 

// A a;
// A&& b = static_cast< A&&>(a);
// A&& c = std::move(a);
// 创建两个无名引用，用来初始化两个右值引用对象

// A& d = a;
// A& e = b;
// 左值引用可以绑定左值

class Test {
public:
    Test() {
        std::cout << "#### construct \n";
    }

    ~Test() {
        std::cout << "#### destruct \n";
    }
};

void test(Test t) 
{
    std::cout << "test function \n";
}

int main(int argc, char *argv[])
{
    {
        Test t;
        // std::move(t);
        // test(std::move(t));
    }
    return 0;
}
