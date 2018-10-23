#include <iostream>

template<int B, int N>
struct Pow {
    // recursive call and recombination. 
    enum { 
        value = B*Pow<B, N-1>::value
    }; 
}; 
template<int B>
struct Pow<B, 0> {
   // ''N == 0'' condition of termination. 
   enum {
       value = 1 
   };
}; 

template <bool B>
struct Test {
    template <typename T1> int do_it(T1) { 
        std::cout << "Test1-1" << std::endl;
        return 0; 
    }
    template <typename T1, typename T2> int do_it(T1, T2) { 
        std::cout << "Test1" << std::endl;
        return 0; 
    }
};

template <>
struct Test<true> {
    template <typename T1, typename T2> int do_it(T1, T2) { 
        std::cout << "Test2" << std::endl;
        return 0; 
    }
};

// error: no matching function for call to ‘Test<false>::do_it(int)’
// candidate is:
//
// template <>
// struct Test<false> {
//     template <typename T1, typename T2> int do_it(T1, T2) { 
//         std::cout << "Test2" << std::endl;
//         return 0; 
//     }
// };

int main(int argc, char *argv[])
{
    // error:  In instantiation of ‘struct Pow<3, 20>’:
    // int quartic_of_three = Pow<3, 21>::value; 
    
    int quartic_of_three = Pow<3, 19>::value; 

    Test<false> t1;
    t1.do_it(10, 20); // Test1
    t1.do_it(10);
    Test<true> t2;
    t2.do_it(10, 20); // Test2
    // error: no matching function for call to ‘Test<true>::do_it(int)’
    // t2.do_it(10);
    
    Test<std::is_integral<int>::value && std::is_floating_point<float>::value> t3;
    t3.do_it(10, 10.0);
    return 0;
}
