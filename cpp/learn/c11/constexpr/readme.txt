
https://www.cnblogs.com/cauchy007/p/4966067.html

将变量声明为constexpr类型以便由编译器来验证变量是否是一个常量表达式（不会改变，在编译过程中就能得到计算结果的表达式）。
是一种比const更强的约束，这样可以得到更好的效率和安全性。

总结：constexpr修饰的函数，不能依赖任何运行期的信息，不要定义任何变量常量，并且必须尽量简单，要不就会编译不过或告警（坑）。


总结：constexpr修饰的常量必须在编译期确定值，上面的例子也体现出了和const之间的差别。const既可以在编译期确定如ctempA，
也可以在运行期确定如ctempB，使用范围更广。还有一点constexpr只能修饰字面值类型如算数类型、引用类型、指针以及后面介绍的字面值常量类.


总结：constexpr指针不能用局部变量赋值，const指针可以；constexpr指针里是顶层const，即指针是常量，而不是所指向的类型是常量，
如果要指向的类型也为常量，要用constexpr const来修饰。


总结：简单的说constexpr所引用的对象必须在编译期就决定地址。还有一个奇葩的地方就是可以通过上例conexprPtrD来修改g_tempA的值，
也就是说constexpr修饰的引用不是常量，如果要确保其实常量引用需要constexpr const来修饰。
