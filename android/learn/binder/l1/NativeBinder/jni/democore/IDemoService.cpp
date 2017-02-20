#include "IDemoService.h"
#include "utils/String8.h"

namespace android {

enum {
    SHOW_TXT = IBinder::FIRST_CALL_TRANSACTION,

};

class BpDemoService : public BpInterface<IDemoService> {
public:
    BpDemoService(const sp<IBinder>& impl);
    virtual int show(const char* txt);
};

BpDemoService::BpDemoService(const sp<IBinder>& impl) 
    : BpInterface<IDemoService>(impl) 
{

}

int 
BpDemoService::show(const char* txt) 
{
    String8 str(txt);
    Parcel data, reply;
    data.writeInterfaceToken(IDemoService::getInterfaceDescriptor());
    data.writeString8(str);
    remote()->transact(SHOW_TXT, data, &reply);
    return reply.readInt32();
}

IMPLEMENT_META_INTERFACE(DemoService, SERVER_PACK_NAME);

status_t BnDemoService::onTransact(uint32_t code, const Parcel &data, Parcel *reply, uint32_t flags)
{
    switch (code) {
    case SHOW_TXT:
        data.checkInterface(this); //associated to 'writeInterfaceToken'
        reply->writeInt32(show(data.readString8())); 
        break;
    default:
        return BBinder::onTransact(code, data, reply, flags);
    }
    return 0;
}

}
