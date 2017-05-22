#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <sys/types.h>

static int g_pid = 0;
static char s_buff[1024] = { 0 };

void *fn(void *args) 
{
    malloc(100); // 
    sleep(300);  // 
    return (void*)0;
}

void* threadFunc(void* arg) 
{
    printf("Before malloc in thread, threadFunc = %p\n", threadFunc);
    system((const char*)s_buff);
    getchar();
    char buff[1024] = { 0 };
    char* addr = (char*) malloc(127 * 1024);
    system((const char*)s_buff);
    printf("After malloc and before free in thread, addr = %p, buff(小于128K) = %p [mmap heap(thread arena)]\n", addr, buff);
    getchar();
    free(addr);

    char* addr1 = (char*)malloc(127 * 1024);
    char* addr2 = (char*)malloc(127 * 1024);
    char* addr3 = (char*)malloc(127 * 1024);
    system((const char*)s_buff);
    printf("Malloc addr1 addr2 addr3 (127K) in thread");

    getchar();
    free(addr1);
    free(addr2);
    free(addr3);
    system((const char*)s_buff);
    printf("Free addr1 addr2 addr3\n");
    getchar();

    printf("After free in thread.\n");
    system((const char*)s_buff);
    getchar();
    return (void*)0;
}

// cat /proc/self/maps 观察地址落在哪些区域
// glibc ptmalloc2 ，支持多线程堆管理 (dlmalloc不支持)
int main() 
{
    pthread_t t1;
    void* s;
    int ret;
    char* addr;
    char* addr1;
    char* addr2;
    char* addrx;
    int i = 0;
    char buff[1024] = { 0 };
    g_pid = getpid();

    addr = (char*) malloc(127 * 1024); // 小于128K在main arena分配， 默认main arena 132K (也有可能是256K)
    addrx = (char*) malloc(129 * 1024);

    sprintf(s_buff, "cat /proc/%d/maps", g_pid);
    system((const char*)s_buff);
    printf("\npid = [%d]\n\t main = %p [ro code], addr(小于128K) = %p [sbrk heap(main arena)]," 
        "addrx(大于128K) = %p [mmap heap], \n\t"
        "buff = %p [stack], s_buff = %p [static], i = %p [stack] g_pid = %p\n", 
        getpid(), main, addr, addrx, buff, s_buff, &i, &g_pid);
    getchar();
#if 1
    // 下面实践把132K(or 256K)的main arena heap 用完
    addr1 = (char*) malloc(127 * 1024); // 小于128K在main arena分配
    addr2 = (char*) malloc(127 * 1024); // 小于128K在main arena分配
    system((const char*)s_buff);
    printf("addr1 = %p [heap] addr2 = %p [heap] **** 会发现heap地址区域变大 ***** \n", addr1, addr2); // 一直增长， 直到发生内存不够

    getchar();

    free(addr1);
    free(addr2);
    printf("Free addr1 addr2 (又恢复了默认的main arena 大小)\n");
    system((const char*)s_buff);
    getchar();

#endif

    free(addr);
    printf("After free addr in main thread, *** heap 内存没有释放给操作系统, *** \n"); // 没有释放给操作系统, 而是是释放给glibc malloc
    system((const char*)s_buff);
    getchar();

    ret = pthread_create(&t1, NULL, threadFunc, NULL);
    if (ret) {
        printf("Thread creation error\n");
        return -1;
    }
    ret = pthread_join(t1, &s);
    if (ret) {
        printf("Thread join error\n");
        return -1;
    }


    const int num = 16;
    pthread_t pids[num];
    for (i = 0; i < num; i++) {
        pthread_create(&pids[i], NULL, fn, NULL);
    }
    sleep(3);
    printf("Create %d phreads\n", num);
    system((const char*)s_buff);

    for (i = 0; i < num; i++) {
        pthread_join(pids[i], NULL);
    }
    return 0;
}

// https://zhuanlan.zhihu.com/p/24790164
// https://zhuanlan.zhihu.com/p/24753861
// http://www.hulkdev.com/posts/glibc-basic
// http://fanrong1992.github.io/2016/04/11/%E6%B7%B1%E5%85%A5%E7%90%86%E8%A7%A3glibc-malloc/
// https://sploitfun.wordpress.com/2015/02/10/understanding-glibc-malloc/
// http://paper.seebug.org/255/  (推荐)
