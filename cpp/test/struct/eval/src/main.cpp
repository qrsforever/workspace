#include <stdio.h>

struct A {
    int a;
    char* p;
};

int main(int argc, char *argv[])
{
    char base[] = {"aa"};
    A a = {10, base};    
    A b = a; 
    printf("a(%d %p) vs  b(%d %p)\n", a.a, a.p, b.a, b.p);
    return 0;
}
