#include <iostream>
#include <utility>

class MemoryBlock
{
public:

    // 构造器（初始化资源）
    explicit MemoryBlock(size_t length)
        : _length(length)
          , _data(new int[length])
    {
        std::cout << "MemoryBlock construct \n";
    }

    // 析构器（释放资源）
    ~MemoryBlock()
    {
        std::cout << "MemoryBlock destruct " << _data << "\n";
        if (_data != nullptr)
        {
            delete[] _data;
        }
    }

    // 拷贝构造器（实现拷贝语义：拷贝that）
    MemoryBlock(const MemoryBlock& that)
        // 拷贝that对象所拥有的资源
        : _length(that._length)
          , _data(new int[that._length])
    {
        std::copy(that._data, that._data + _length, _data);
        std::cout << "MemoryBlock const MemoryBlock) \n";
    }

    // 拷贝赋值运算符（实现拷贝语义：释放this ＋ 拷贝that）
    MemoryBlock& operator=(const MemoryBlock& that)
    {
        std::cout << "MemoryBlock operator = \n";
        if (this != &that)
        {
            // 释放自身的资源
            delete[] _data;

            // 拷贝that对象所拥有的资源
            _length = that._length;
            _data = new int[_length];
            std::copy(that._data, that._data + _length, _data);
        }
        return *this;
    }

    // 移动构造器（实现移动语义：移动that）
    MemoryBlock(MemoryBlock&& that)
        // 将自身的资源指针指向that对象所拥有的资源
        : _length(that._length)
          , _data(that._data)
    {
        std::cout << "MemoryBlock &&\n";
        // 将that对象原本指向该资源的指针设为空值
        that._data = nullptr;
        that._length = 0;
    }

    // 移动赋值运算符（实现移动语义：释放this ＋ 移动that）
    MemoryBlock& operator=(MemoryBlock&& that)
    {
        std::cout << "MemoryBlock =&&\n";
        if (this != &that)
        {
            // 释放自身的资源
            delete[] _data;

            // 将自身的资源指针指向that对象所拥有的资源
            _data = that._data;
            _length = that._length;

            // 将that对象原本指向该资源的指针设为空值
            that._data = nullptr;
            that._length = 0;
        }
        return *this;
    }
private:
    size_t _length; // 资源的长度
    int* _data; // 指向资源的指针，代表资源本身
};

MemoryBlock f() 
{ 
    return MemoryBlock(50); 
}

int main(int argc, char *argv[])
{
    std::cout << "1\n";
    MemoryBlock a = f();            // ??error: 调用移动构造器，移动语义
    std::cout << "2\n";
    MemoryBlock b = a;              // 调用拷贝构造器，拷贝语义
    std::cout << "3\n";
    MemoryBlock c = std::move(a);   // 调用移动构造器，移动语义
    std::cout << "4\n";
    a = f();                        // 调用移动赋值运算符，移动语义
    std::cout << "5\n";
    b = a;                          // 调用拷贝赋值运算符，拷贝语义
    std::cout << "6\n";
    c = std::move(a);               // 调用移动赋值运算符，移动语义
    std::cout << "7\n";
    return 0;
}

// output:
// 1
// MemoryBlock construct 
// 2
// MemoryBlock const MemoryBlock) 
// 3
// MemoryBlock &&
// 4
// MemoryBlock construct 
// MemoryBlock =&&
// MemoryBlock destruct 0
// 5
// MemoryBlock operator = 
// 6
// MemoryBlock =&&
// 7
// MemoryBlock destruct 0x14d2dc0
// MemoryBlock destruct 0x14d2cf0
// MemoryBlock destruct 0

// 参考: https://blog.csdn.net/viggirl/article/details/52858108

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


