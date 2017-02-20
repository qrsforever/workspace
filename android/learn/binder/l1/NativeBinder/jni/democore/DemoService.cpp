#include "DemoService.h"
#include <stdio.h>

namespace android {

DemoService::DemoService() 
{
}

DemoService::~DemoService() 
{
}

int 
DemoService::show(const char* txt)
{
    if (txt)
        printf("DemoService: show[%s]\n", txt);
    return 100;
}

}
