#include <stdio.h>
#include <string.h>

#ifndef HAVE_STRLCPY
size_t strlcpy(char *dst, const char *src, size_t size);
#endif

#define MAX_LEN 32
int main(int argc, char ** argv)
{
    char a1[48] = "com.letv.tvos.gamecenter:de_service"; 
    char b1[MAX_LEN] = "com.letv.tvos.gamecenter:de_se";
    char d1[MAX_LEN] = { 0 };

    strncpy(d1, a1, MAX_LEN-1);
    printf("[%s] vs [%s] = %d\n", d1, a1, strncmp(d1, a1, MAX_LEN));
    printf("[%s] vs [%s] = %d\n", d1, a1, strncmp(d1, a1, MAX_LEN-1));

    strlcpy(d1, a1, MAX_LEN);
    printf("[%s] vs [%s] = %d\n", d1, a1, strncmp(d1, a1, MAX_LEN));
    printf("[%s] vs [%s] = %d\n", d1, a1, strncmp(d1, a1, MAX_LEN-1));

    return 0;
}
