#include "foo.h"


Foo::Foo()
{
}

Foo::~Foo()
{

}

int Foo::test()
{
    return 1;
}

#ifndef ONE
int Foo::init()
{
    return 100;
}
#endif
