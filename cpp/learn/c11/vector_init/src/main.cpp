#include <vector>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
    /*1.空vector<int>*/
    vector<int> vecTemp1;

    /*2.10个0*/
    vector<int> vecTemp2(10);

    /*3.1个10*/
    vector<int> vecTemp3{10};

    /*4.10个42*/
    vector<int> vecTemp4(10,42);

    /*5.列表初始化10,42*/
    vector<int> vecTemp5{10,42};

    /*6.10个空string*/
    vector<string> vecTemp6{10};

    /*7.10个“hi”*/
    vector<string> vecTemp7{10, "hi"};
    return 0;
}
