#include <iostream>

using namespace std;

class A {
public:
    A() {};
    virtual ~A() {};

private:
    
}; /* class A */

class B: public A {
public:
    B() {};
    virtual ~B(){};

private:
    
}; /* class B: public A */

class C: public A {
public:
    C(){};
    virtual ~C(){};

private:
    
}; /* class C: public A */

int main(int argc, char *argv[])
{
    B b;    
    A* a = &b;
    B* b1 = dynamic_cast<B*>(a);
    cout << b1 << endl; // ok
    C* c1 = dynamic_cast<C*>(a);
    cout << c1 << endl; // 0
    return 0;
}
