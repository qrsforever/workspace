#include <stdlib.h>
#include <iostream>
#include <string>

using namespace std;

extern "C" void test_deftemplate_sample();
extern "C" void test_defclass_sample();

int main(int argc, char *argv[])
{
    string select;     

    cout << "  1. test deftemplate sample" << endl;
    cout << "  2. test defclass sample" << endl;
    cout << "Input: ";
    cin >> select;

    switch (atoi(select.c_str())) {
    case 1:
        test_deftemplate_sample();
        break;
    case 2:
        test_defclass_sample();
        break;
    default:
        ;
    }
    return 0;
}
