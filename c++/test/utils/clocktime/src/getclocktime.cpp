#include <stdio.h>
#include <time.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    printf("ts.tv_sec=%ld\n", ts.tv_sec);
    uint32_t ms = (ts.tv_sec * 1000) + (ts.tv_nsec / 1000000); 
    printf("clock time[%u]\n", ms);
    return 0;
}
