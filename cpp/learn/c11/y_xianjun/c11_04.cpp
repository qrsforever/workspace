#include <iostream>


int GetFive() {return 5;}

constexpr int CGetFive() {return 5;}

// Error: array bound is not an integer constant before ‘]’ token
// int values[GetFive() + 10];
int values[CGetFive() + 10];

int main(int argc, char *argv[])
{
    // OK
    int values1[GetFive() + 10];
    int values2[CGetFive() + 10];
    return 0;
}
