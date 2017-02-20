#include <stdio.h>
#include <binder/IPCThreadState.h>
#include <binder/ProcessState.h>
#include <binder/IServiceManager.h>
#include "IDemoService.h"

using namespace android;

int main(int argc, char const* argv[])
{
    sp<IServiceManager> sm = defaultServiceManager();
    sp<IBinder> binder;
    if ((binder = sm->getService(String16(SERVER_PACK_NAME))) == 0) {
        printf("### Cannot get %s Service!\n", SERVER_PACK_NAME);
        return -1;
    }
    sp<IDemoService> sDemoService = interface_cast<IDemoService>(binder);
    ProcessState::self()->startThreadPool();
    int ret = sDemoService->show("Hello World");
    printf("### get result = %d\n", ret);
    IPCThreadState::self()->flushCommands();
    while (1);
    return 0;
}
