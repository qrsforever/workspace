#include <iostream>
#include <memory>


class Object {
public:
    Object() {
    }

    // must virtual
    virtual ~Object() {
    }

};

class StringData : public Object {
public:
    StringData() {
        std::cout << "StringData()" << std::endl;
    }

    ~StringData() {
        std::cout << "~StringData()" << std::endl;
    }

    void test() {
        std::cout << "test" << std::endl;
    }
};

void test(std::shared_ptr<Object> o)
{
    // dynamic_pointer_cast
    std::shared_ptr<StringData> data(std::dynamic_pointer_cast<StringData>(o));
    // std::shared_ptr<StringData> data(std::static_pointer_cast<StringData>(o));
    data->test();
}

void run()
{
    // std::shared_ptr<StringData> data(std::make_shared<StringData>()); 
    auto data(std::make_shared<StringData>()); 
    test(data);
    std::cout << "run end!" << std::endl;
}

struct BaseClass {};
 
struct DerivedClass : BaseClass
{
    void f() const
    {
        std::cout << "Hello World!\n";
    }
    ~DerivedClass(){ // 注意：它不是虚的
        std::cout << "~DerivedClass\n";
    }
};
 
int main(int argc, char *argv[])
{
    run();
    
    // std::shared_ptr<BaseClass> ptr_to_base(std::make_shared<DerivedClass>());
 
    // // ptr_to_base->f(); // 错误不会编译： BaseClass 无名为 'f' 的成员
 
    // std::static_pointer_cast<DerivedClass>(ptr_to_base)->f(); // OK
    // // （构造临时 shared_ptr ，然后调用 operator-> ）
 
    // static_cast<DerivedClass*>(ptr_to_base.get())->f(); // 亦 OK
    // // （直接转型，不构造临时 shared_ptr ）
    return 0;
}

