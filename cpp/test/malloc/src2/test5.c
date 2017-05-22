#include<stdio.h>
#include<stdlib.h>
int main()  
{
    void *m1 = malloc(500);
    void *m2 = malloc(40);
    malloc(1);
    void *m3 = malloc(80);
    free(m1);
    free(m2);
    void *m4 = malloc(40);

    free(m3);
    void *m5 = malloc(80);
    printf("m1, %p\n",m1);
    printf("m2, %p\n",m2);
    printf("m3, %p\n",m3);
    printf("m4, %p\n",m4);
    printf("m5, %p\n",m5);

    return 0;
}
