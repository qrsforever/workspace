#include <iostream>
#include <utility>
#include <typeinfo>

// fails https://www.cnblogs.com/gtarcoder/p/4805692.html
using namespace std;

template<typename T>
void print(T& t)
{
	cout << "lvalue" << endl;
}

template<typename T>
void print(T&& t)
{
	cout << "rvalue" << endl;
}

template<typename T>
void TestForward(T&& v)
{
    // cout << typeid(v).name() << endl;
    print(v);
	// print(std::forward<T>(v));
	print(std::move(v));
}

int main(int argc, char *argv[])
{
    // print(1);
    TestForward(1);
    int x = 1;
    TestForward(x);
	// TestForward(std::forward<int>(x));
	return 0;
}
