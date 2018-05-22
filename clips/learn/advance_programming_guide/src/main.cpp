#include <stdlib.h>
#include <iostream>
#include <string>

using namespace std;

extern "C" void test_simple_sample();

int main(int argc, char *argv[])
{
    string select;     

    cout << "  1. test deftemplate sample" << endl;
    cout << "Input: ";
    cin >> select;


    switch (atoi(select.c_str())) {
    case 1:
        test_deftemplate_sample();
        break;
    default:
        ;
    }
    return 0;
}
