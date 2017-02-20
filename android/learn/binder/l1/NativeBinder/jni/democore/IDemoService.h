#ifndef __ANDROID_IDEMO_SERVICE_H__
#define __ANDROID_IDEMO_SERVICE_H__

#include <binder/IInterface.h>
#include <binder/Parcel.h>

#define SERVER_PACK_NAME "android.test.demoservice"

namespace android {

class IDemoService : public IInterface {
public:
    DECLARE_META_INTERFACE(DemoService);
    virtual int show(const char* txt) = 0;
};

class BnDemoService : public BnInterface<IDemoService> {
public:
    virtual status_t onTransact(uint32_t code,
                                const Parcel &data,
                                Parcel *reply,
                                uint32_t flags = 0);
};

}
#endif
