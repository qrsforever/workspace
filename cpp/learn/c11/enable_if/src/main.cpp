#include <iostream>
#include <type_traits>

// 实现: 如果条件为真, 定义类型T
/* template<bool Cond, typename T = void> struct enable_if {};
 * template<typename T> struct enable_if<true, T> { typedef T type; }; */

 // 1. the return type (bool) is only valid if T is an integral type: template <class T> typename
 // std::enable_if<std::is_integral<T>::value,bool>::type is_odd (T i) {return bool(i%2);}


// enable_if example: two ways of using enable_if
#include <iostream>
#include <type_traits>

// 1. the return type (bool) is only valid if T is an integral type:
template <class T>
typename std::enable_if<std::is_integral<T>::value,bool>::type
  is_odd (T i) {return bool(i%2);}

// 2. the second template argument is only valid if T is an integral type:
template < class T,
           class = typename std::enable_if<std::is_integral<T>::value>::type>
bool is_even (T i) {return !bool(i%2);}

int main(int argc, char *argv[])
{
	short int i = 1;    // code does not compile if type of i is not integral

    std::cout << std::boolalpha;
	std::cout << "i is odd: " << is_odd(i) << std::endl;
	std::cout << "i is even: " << is_even(11) << std::endl;
    // error
	// std::cout << "i is even: " << is_even(10.01f) << std::endl;

	return 0;
}
