#include <iostream>


class A
{
public:
    A () {}
    ~A () {}
    void Acall_public_method(const char* from) { std::cout << "A.call_public_method from " << from << std::endl; }

protected:
    void Acall_protected_method(const char* from) { std::cout << "A.call_protected_method from " << from << std::endl; }

private:
    void Acall_private_method(const char* from) { std::cout << "A.call_private_method from " << from << std::endl; }
};

class B : protected A
{
public:
    B () {}
    ~B () {}
    void Bcall_public_method(const char* from) { 
        std::cout << "B.call_public_method from " << from << std::endl; 
        A::Acall_public_method("B"); // OK
        A::Acall_protected_method("B"); // OK
        // A::call_private_method("B"); // Error
    }
};

class C : private A
{
public:
    C () {}
    ~C () {}
    void Ccall_public_method(const char* from) { 
        std::cout << "C.call_public_method from " << from << std::endl; 
        A::Acall_public_method("C"); // OK
        A::Acall_protected_method("C"); // OK
        // A::call_private_method("C"); // Error
    }
};

class BB : public B
{
public:
    BB () {}
    ~BB () {}
    void BBcall_public_method(const char* from) { 
        std::cout << "BB.call_public_method from " << from << std::endl; 
        A::Acall_public_method("BB"); // OK
        A::Acall_protected_method("BB"); // OK
        // A::call_private_method("BB"); // Error
    }
};

class CC : public C
{
public:
    CC () {}
    ~CC () {}
    void CCcall_public_method(const char* from) { 
        std::cout << "CC.call_public_method from " << from << std::endl; 
        // A::Acall_public_method("CC"); // Error private 私有继承， 即使内部也无法访问
        // A::Acall_protected_method("CC"); // Error
        // A::call_private_method("CC"); // Error
    }
};

int main(int argc, char *argv[])
{
    B b; 
    b.Bcall_public_method("Main");
    // b.Acall_public_method("Main"); // Error protected继承， 外界访问不了
    C c;
    c.Ccall_public_method("Main");

    BB bb;
    bb.Bcall_public_method("Main");
    return 0;
}
