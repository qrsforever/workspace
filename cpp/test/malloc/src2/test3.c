#include<stdio.h>                                                                                                                                                                                                  
#include<stdlib.h>                                                                                                                                                                                                 
#include<string.h>                                                                                                                                                                                                 

int main()  
{
    void * m1 = malloc(0x80-8);                                                                                                                                                                                    
    void * m2 = malloc(0x80-8);                                                                                                                                                                                    
    memset(m1, 65, 0x80-8);                                                                                                                                                                                        
    memset(m2, 65, 0x80-8);                                                                                                                                                                                        
    malloc(1);                                                                                                                                                                                                     
    free(m1);                                                                                                                                                                                                      
    free(m2);                                                                                                                                                                                                      
    printf("m1: %p\n", m1);                                                                                                                                                                                        
    printf("m2: %p\n", m2);                                                                                                                                                                                        
    printf("sizeof(size_t): %ld\n", sizeof(size_t));                                                                                                                                                               

    return 0;
}
