#include <iostream>
#include <stdlib.h>

using namespace std;

/*1.如果size在编译时能确定，那么返回值就可以是constexpr,编译通过*/
constexpr int getSizeA(int size)
{
    return 4*size;
}

#if 0 /* function */

/*2.编译通过，有告警：在constexpr中定义变量*/
/* error: body of constexpr function ‘constexpr int getSizeB(int)’ not a return-statement */
constexpr int getSizeB(int size)
{
    int index = 0;
    return 4;
}

/*3.编译通过，有告警：在constexpr中定义变量（这个有点迷糊）*/
/* error: body of constexpr function ‘constexpr int getSizeB(int)’ not a return-statement */
constexpr int getSizeC(int size)
{
    constexpr int index = 0;
    return 4;
}

/*4.编译通过，有告警：使用了if语句（使用switch也会告警）*/
/* error: body of constexpr function ‘constexpr int getSizeB(int)’ not a return-statement */
constexpr int getSizeD(int size)
{
    if(0)
    {}
    return 4;
}

/*5.定义变量并且没有初始化，编译不过*/
/* error: body of constexpr function ‘constexpr int getSizeB(int)’ not a return-statement */
constexpr int getSizeE(int size)
{
    int index;
    return 4;
}

/*6.rand()为运行期函数，不能在编译期确定，编译不过*/
/* error: call to non-constexpr function ‘int rand()’ */
constexpr int getSizeF(int size)
{
    return 4*rand();
}

/*7.使用了for，编译不过*/
constexpr int getSizeG(int size)
{
    for(;0;)
    {}
    return 4*rand();
}
#endif

void test_type()
{
    int tempA;
    cin >> tempA;

    const int ctempA = 4;
    const int ctempB = tempA;

    /*1.可以再编译器确定，编译通过*/
    constexpr int conexprA = 4;
    constexpr int conexprB = conexprA + 1;
    constexpr int conexprC = getSizeA(conexprA);
    constexpr int conexprD = ctempA;

    /*2.不能在编译期决定，编译不过*/
    /* constexpr int conexprE = tempA; */
    /* constexpr int conexprF = ctempB; */
}

int g_tempA = 4;
const int g_conTempA = 4;
constexpr int g_conexprTempA = 4;

int test_pointer()
{
    int tempA = 4;
    const int conTempA = 4;
    constexpr int conexprTempA = 4;

    /*1.正常运行,编译通过*/
    const int *conptrA = &tempA;
    const int *conptrB = &conTempA;
    const int *conptrC = &conexprTempA;

    /*2.局部变量的地址要运行时才能确认，故不能在编译期决定，编译不过*/
    /* constexpr int *conexprPtrA = &tempA; */
    /* constexpr int *conexprPtrB = &conTempA */
    /* constexpr int *conexprPtrC = &conexprTempA; */

    /*3.第一个通过，后面两个不过,因为constexpr int *所限定的是指针是常量，故不能将常量的地址赋给顶层const*/
    constexpr int *conexprPtrD = &g_tempA;
    /* error: invalid conversion from ‘const int*’ to ‘int*’ [-fpermissive] */
    /* constexpr int *conexprPtrE = &g_conTempA; */
    /* error: invalid conversion from ‘const int*’ to ‘int*’ [-fpermissive] */
    /* constexpr int *conexprPtrF = &g_conexprTempA; */

    /*4.局部变量的地址要运行时才能确认，故不能在编译期决定，编译不过*/
    /* error: is not a constant expression */
    /* constexpr const int *conexprConPtrA = &tempA; */
    /* constexpr const int *conexprConPtrB = &conTempA; */
    /* constexpr const int *conexprConPtrC = &conexprTempA; */

    /*5.正常运行，编译通过*/
    constexpr const int *conexprConPtrD = &g_tempA;
    constexpr const int *conexprConPtrE = &g_conTempA;
    constexpr const int *conexprConPtrF = &g_conexprTempA;

    return 0;
}

int test_ref(void)
{
    int tempA = 4;
    const int conTempA = 4;
    constexpr int conexprTempA = 4;

    /*1.正常运行，编译通过*/
    const int &conptrA = tempA;
    const int &conptrB = conTempA;
    const int &conptrC = conexprTempA;

    /*2.有两个问题：一是引用到局部变量，不能再编译器确定；二是conexprPtrB和conexprPtrC应该为constexpr const类型，编译不过*/
    /* error: ‘* & tempA’ is not a constant expression */
    /* constexpr int &conexprPtrA = tempA; */
    /* error: invalid initialization of reference of type ‘int&’ from expression of type ‘const int’ */
    /* constexpr int &conexprPtrB = conTempA; */
    /* error: error: invalid initialization of reference of type ‘int&’ from expression of type ‘const int’ */
    /* constexpr int &conexprPtrC = conexprTempA; */

    /*3.第一个编译通过，后两个不通过，原因是因为conexprPtrE和conexprPtrF应该为constexpr const类型*/
    constexpr int &conexprPtrD = g_tempA;
    /* constexpr int &conexprPtrE = g_conTempA; */
    /* constexpr int &conexprPtrF = g_conexprTempA; */

    /*4.正常运行，编译通过*/
    constexpr const int &conexprConPtrD = g_tempA;
    constexpr const int &conexprConPtrE = g_conTempA;
    constexpr const int &conexprConPtrF = g_conexprTempA;

    return 0;
}

int main(int argc, char *argv[])
{
    test_type();
    test_pointer();
    test_ref();
    return 0;
}
