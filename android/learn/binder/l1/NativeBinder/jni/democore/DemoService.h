#ifndef __ANDROID_DEMOSERVICE_H__
#define __ANDROID_DEMOSERVICE_H__

#include "IDemoService.h"

namespace android {

class DemoService : public BnDemoService {
public:
    DemoService();
    ~DemoService();
    virtual int show(const char* txt);
};

}

#endif
