
#include <vector>
#include <iostream>

int main(int argc, char *argv[])
{
    std::vector<char*> c_strings;
    c_strings.push_back("ls");
    c_strings.push_back("-l");
    char ** p = c_strings.data();
    std::cout << *p << std::endl;
    std::cout << *(++p) << std::endl;
    return 0;
}
