#include <stdio.h>
#include <iostream>  
#include <stdarg.h>  
#include <string.h>  
using namespace std;  

void func(const char *c,...){  

    int i=0;  
    double result=0;  
    va_list arg;    //va_list变量  
    va_start(arg,c);    //arg指向固定参数c  
    while(c[i]!='\0'){  

        if(c[i]=='%'&&c[i+1]=='d'){  
            printf("%d",va_arg(arg,int));  
            i++;  
        }  
        else if(c[i]=='%'&&c[i+1]=='f'){  
            printf("%f",va_arg(arg,double));  
            i++;  
        }     
        else
            putchar(c[i]);  
        i++;  
    }  
    va_end(arg);  
}  


int main(int, char**)
{  
    int i=100;  
    int is[2] = { 100, 200 };
    double j=100.0;  
    printf("%d %d be equal %f\n",i, is[1],j);  
    func("%d %d %d be equal %f\n", is, j);
    return 0;
}
