#include <iostream>

using namespace std;

int getSize();

void test_base()
{
    int tempA = 2;

    /*1.dclTempA为int*/
    decltype(tempA) dclTempA;

    /*2.dclTempB为int，对于getSize根本没有定义，但是程序依旧正常，因为decltype只做分析，并不调用getSize，*/
    decltype(getSize()) dclTempB;
}

void test_with_const()
{
	double tempA = 3.0;
    const double ctempA = 5.0;
    const double ctempB = 6.0;
    const double *const cptrTempA = &ctempA;

    /*1.dclTempA推断为const double（保留顶层const，此处与auto不同）*/
    decltype(ctempA) dclTempA = 4.1;

    /*2.dclTempA为const double，不能对其赋值，编译不过*/
    /* dclTempA = 5; */

    /*3.dclTempB推断为const double * const*/
    decltype(cptrTempA) dclTempB = &ctempA;

    /*4.输出为4（32位计算机）和5*/
    cout << sizeof(dclTempB) << "    " << *dclTempB << endl;

    /*5.保留顶层const，不能修改指针指向的对象，编译不过*/
    /* dclTempB = &ctempB; */

    /*6.保留底层const，不能修改指针指向的对象的值，编译不过*/
    /* *dclTempB = 7.0; */
}

void test_with_ref()
{
	int tempA = 0, &refTempA = tempA;

    /*1.dclTempA为引用，绑定到tempA*/
    decltype(refTempA) dclTempA = tempA;

    /*2.dclTempB为引用，必须绑定到变量，编译不过*/
    /* decltype(refTempA) dclTempB = 0; */

    /*3.dclTempC为引用，必须初始化，编译不过*/
    /* decltype(refTempA) dclTempC; */

    /*4.双层括号表示引用，dclTempD为引用，绑定到tempA*/
    decltype((tempA)) dclTempD = tempA;

    const int ctempA = 1, &crefTempA = ctempA;

    /*5.dclTempE为常量引用，可以绑定到普通变量tempA*/
    decltype(crefTempA) dclTempE = tempA;

    /*6.dclTempF为常量引用，可以绑定到常量ctempA*/
    decltype(crefTempA) dclTempF = ctempA;

    /*7.dclTempG为常量引用，绑定到一个临时变量*/
    decltype(crefTempA) dclTempG = 0;

    /*8.dclTempH为常量引用，必须初始化，编译不过*/
    /* decltype(crefTempA) dclTempH; */

    /*9.双层括号表示引用,dclTempI为常量引用，可以绑定到普通变量tempA*/
    decltype((ctempA)) dclTempI = ctempA;
}

void test_with_pointer()
{
    int tempA = 2;
    int *ptrTempA = &tempA;

    /*1.常规使用dclTempA为一个int *的指针*/
    decltype(ptrTempA) dclTempA;

    /*2.需要特别注意，表达式内容为解引用操作，dclTempB为一个引用，引用必须初始化，故编译不过*/
    /* decltype(*ptrTempA) dclTempB; */
}

int main(int argc, char *argv[])
{
    test_base();
    test_with_const();
    test_with_ref();
    test_with_pointer();
    return 0;
}
