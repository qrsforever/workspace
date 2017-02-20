#include <stdio.h>

#include <binder/IPCThreadState.h>
#include <binder/ProcessState.h>
#include <binder/IServiceManager.h>
#include "DemoService.h"

using namespace android;

int main(int argc, char const* argv[])
{
    sp<IServiceManager> sm = defaultServiceManager();     
    sm->addService(String16(SERVER_PACK_NAME), new DemoService());
    sp<ProcessState> proc(ProcessState::self());
    ProcessState::self()->startThreadPool();
    IPCThreadState::self()->joinThreadPool();
    return 0;
}
