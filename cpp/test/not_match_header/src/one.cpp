#include "one.h"

One::One()
{
    foo = new Foo();
}

One::~One()
{

}

int One::test()
{
    return foo->test();
}

