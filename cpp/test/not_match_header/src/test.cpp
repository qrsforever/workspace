#include <stdio.h>
#include "one.h"
#include "foo.h"

int main(int argc, char *argv[])
{
    One *one = new One();  
    printf("####%d\n", one->test());
    return 0;
}
