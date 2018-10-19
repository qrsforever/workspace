使用 auto/decltype/result_of使代码可读易维护

http://www.cnblogs.com/qicosmos/p/3286057.html

auto和decltype只是占位符的作用，告诉编译器这个变量的类型需要编译器推导.

auto不能解决精度问题


decltype主要为库作者所用，但是如果是我们需要用template，那么使用它也能简洁我们的代码。


template <_Ty>
typenamea add_rvalue_reference<_Ty>::type declval() _noexcept;

其中，add_rvalue_reference为一个traits，定义为

template <_Ty>
struct add_rvalue_reference
{
    typedef _Ty&& type;
}

declval实际上是等同于实例化了这个类型的一个对像，进而可以用这个对像调用成员方法，成员变量。这个方法最妙的地方在于不论类型的构造如何定义甚至
有无构造都能获得这个类型的一个对像的引用实例。
