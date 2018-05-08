#include <iostream>
#include <vector>
#include <algorithm>

template <class onefunc>
void test_func(onefunc func)
{
    std::cout << "test_func : " << func(2) << std::endl;
}

template <class InputIt, class Function>
Function my_for_each(InputIt first, InputIt last, Function func)
{
    while (first != last) {
        func(*first);
        ++first;
    }
    return func;
}

int main(int argc, char const* argv[])
{

    // format: [capture list](parameter list) -> return type {function body}
    int x = 1, y = 2, z = 3;
    // 测试 [=] 传值
    auto square_sum = [=]() {
        // x++; // error: increment of read-only variable ‘x’
        return x*x + y*y + z*z; // out: 1 + 4 + 9 = 14
    };
    std::cout << "square_sum = " << square_sum() << std::endl;
    // 测试 [&] 传址
    auto incadd_sum = [&]() {
        x++;
        y++;
        z++;
        return x + y + z; // out: 2 + 3 + 4 = 9
    };
    std::cout << "incadd_sum = " << incadd_sum() << std::endl;
    // 测试 [&,y,z]
    auto xadd_multi1 = [&,y,z](int i) {
        x += i;
        // y += i; // error: assignment of read-only variable ‘y’
        // z += i; // error: assignment of read-only variable ‘z’
        return x*y*z; // out: 4*3*4 = 48 (i = 2)
    };
    std::cout << "xadd_multi1 = " << xadd_multi1(2) << std::endl;
    x = 2;
    y = 3;
    z = 4;
    // 测试 lambda实质 也许编译器就是把lambda句式在后面解析生成这样一个类class.
    class AnonymousClass {
    private:
        int& mX;
        const int mY;
        const int mZ;
    public:
        AnonymousClass(int& x, int y, int z)
            : mX(x), mY(y), mZ(z) { }
        int operator() (int i) const {
            mX += i;
            // mY += i; // error: assignment of member ‘AnonymousClass::mY’ in read-only object
            // mZ += i; // error: assignment of member ‘AnonymousClass::mY’ in read-only object
            return mX*mY*mZ; // out: 4*3*4 = 48 (i=2)
        }
    };
    auto xadd_multi2 = AnonymousClass(x, y, z);
    std::cout << "xadd_multi2 = " << xadd_multi2(2) << std::endl;
    // 测试 函数传递
    x = 2;
    test_func(xadd_multi1);
    x = 2;
    test_func(xadd_multi2);
    // C++11里闭包相关函数 sort, std::for_each
    int sum = 0;
    std::vector<int> nums { 1, -3, 5, -7, 9, 2, -4, 6, 8 };
    std::sort(
        nums.begin(),
        nums.end(),
        [](const int &x, const int &y) {
            return abs(x) < abs(y);
        });
    std::for_each(
        nums.begin(),
        nums.end(),
        [&](int &n) {
            std::cout << n << " ";
            sum += n;
        });
    std::cout << std::endl << "sum = " << sum << std::endl;
    // lambda闭包函数的实现
    struct Sum {
        Sum():sum(0) { }
        void operator()(int n) {
            std::cout << n << " ";
            sum += n;
        }
        int sum;
    };
    Sum s = std::for_each(
        nums.begin(),
        nums.end(),
        Sum()
        );
    std::cout << std::endl << "sum = " << s.sum << std::endl;
    // 模拟for_each函数的实现方法
    int sum2 = 0;
    std::vector<int> nums2 { 1, -3, 5, -7, 9, 2, -4, 6, 8 };
    struct CustomCompare {
        CustomCompare() { }
        bool operator()(int a, int b) {
            return abs(a) < abs(b);
        }
    };
    std::sort(
        nums2.begin(),
        nums2.end(),
        CustomCompare()
        );
    my_for_each(
        nums.begin(),
        nums.end(),
        [&](int &n) {
            std::cout << n << " ";
            sum2 += n;
        });
    std::cout << std::endl << "sum = " << sum2 << std::endl;
    return 0;
}

// output:
//  square_sum = 14
//  incadd_sum = 9
//  xadd_multi1 = 48
//  xadd_multi2 = 48
//  test_func : 48
//  test_func : 48
//  1 2 -3 -4 5 6 -7 8 9 
//  sum = 17
//  1 2 -3 -4 5 6 -7 8 9 
//  sum = 17
//  1 2 -3 -4 5 6 -7 8 9 
//  sum = 17

//
// 1. 闭包在编程语言中先出现在面向函数式编程的语种, 比如python, 因为没有类这中能够存放上下文的东西.
//     闭包中使用了某些变量, 这些变量的生命周期不属于这个闭包函数, 但也不受闭包外的生命周期控制.
//
// 2. 闭包定义格式:
//               [capture list](parameter list) -> return type {function body}
//    capture list (捕获上下文变量)
//                     [  ]:  不使用上下文变量
//                     [=] : 变量值捕获, 在闭包函数中是只读的
//                     [&] : 变量址捕获, 可以修改该变量的值
//                     [=, var1, var2...] : 除了var1, var2等列出的上下文变量可读写, 其他变量只读
//                     [&, var1, var2...]:  除了var1, var2等列出的上下文变量只读传递, 其他的变量可读写.
//     parameter list (参数列表)
//      -> return type 闭包函数返回类型
//     {function body} 函数体
//
// 3. C++11之后引入了闭包(lambda)函数, 该改变只是编译器对新句式的解析, 并没有增加新的语义. 编译器默默在后面生成了类.
//
// 4. C++闭包函数的实现机制, 使用类实现, 并且使类重载操作符(), 使其用起来像个函数, 类本身可以存储上下文变量. (纯意淫)
//
// 5. C++闭包的产生是偷懒程序员的结晶, 通过程序对比, 闭包从代码上看确实简练了不少, 让程序员少写好多代码.
//
// 6. 编译选项 -std=c++11
//
// 7. auto 自动推导类型, 大概是因为lambda句式尚不知道编译器生成的类class的名字是什么, 所以只能自动推导变量的类型.
//
// 8. 闭包lambda的实现可以由template<> 模板 和 operate() 操作符重载间接实现, 也许lambda就是这样做的.


