#include <iostream>
#include <string>

std::string& stringTrim(std::string& text)
{
    if (!text.empty()) {
        text.erase(0, text.find_first_not_of((" \n\r\t\f\v")));
        text.erase(text.find_last_not_of((" \n\r\t\f\v")) + 1);
    }
    return text;
}

int main(int argc, char *argv[])
{
    std::string text = "    ff          \n"; 
    std::cout << "[" << stringTrim(text) << "]" << std::endl; 
    return 0;
}
