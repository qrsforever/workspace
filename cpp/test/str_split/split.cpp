#include <string.h>
#include <string>
#include <vector>
#include <iostream>

std::vector<std::string> stringSplit(const std::string &text, const std::string &delim)
{
	std::vector<std::string> ss;
	char *ptr = strtok((char*)text.c_str(), delim.c_str());
	while (ptr) {
		ss.push_back(ptr);
		ptr = strtok(NULL, delim.c_str());
	}
	return std::move(ss);
}

int main(int argc, char *argv[])
{
    std::string a("001;002;003;");
    std::vector<std::string> ss = stringSplit(a, ";");
    for (size_t i = 0; i < ss.size(); ++i) {
        std::cout << ss[i] << std::endl;
    }
    return 0;
}
