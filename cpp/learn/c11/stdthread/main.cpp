#include <iostream>
#include <thread>

void thread_func1(std::string arg1)
{
    std::cout << "thread_func1: " << arg1 << std::endl;
}

void thread_func2(std::string &arg2)
{
    std::cout << "thread_func2: " << arg2 << std::endl;
    arg2 = "change values 2";
}

void thread_func3(std::string &&arg3)
{
    std::cout << "thread_func3: " << arg3 << std::endl;
    arg3 = "change values 3";
}

int main(int argc, char *argv[])
{
    std::cout << "hardware concurrency: " << std::thread::hardware_concurrency() << std::endl;

    std::string arg("Hello");
    std::string arg2("World");
    std::cout << "main thread [" << std::this_thread::get_id() << "], arg = " << arg << ", " << arg2 << std::endl;

    std::thread t1(&thread_func1, arg);
    std::thread t2(&thread_func2, std::ref(arg));
    std::thread t3(&thread_func3, std::move(arg2)); // 内容被释放了, 所以打印为空
    // error: use of deleted function ‘std::thread::thread(std::thread&)’
    // std::thread t4 = t2;
    std::thread t4 = std::move(t2);
    std::cout << "thread1 [" << t1.get_id() << "]" << std::endl;
    std::cout << "thread4 [" << t4.get_id() << "]" << std::endl;
    std::cout << "thread3 [" << t3.get_id() << "]" << std::endl;
    t1.join();
    t4.join();
    t3.join();

    std::cout << "main thread [" << std::this_thread::get_id() << "], arg = " << arg << ", " << arg2 << std::endl;
    return 0;
}
