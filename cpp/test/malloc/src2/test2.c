#include<stdio.h>
#include<stdlib.h>
int main()  
{
    void *m1 = malloc(24);
    int t = 0;
    void * ms[200];

    for(t = 0; t < 200; t++)
        ms[t] = malloc(120); // default fastbin size

    malloc(24);

    for(t = 0; t < 200; t++)
        free(ms[t]);
    void *m2 = malloc(24);
    printf("%p\n",m1);
    printf("%p\n",m2);

    return 0;
}

