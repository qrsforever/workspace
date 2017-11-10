#include <fstream>
#include "addressbook.pb.h"
#include "facestyle.pb.h"

using namespace std;

void FillPerson(tutorial::Person *person,
    const char* name, 
    int id,
    const char* email) 
{
    if (!person)
        return;

    person->set_name(name);
    person->set_id(id);
    person->set_email(email);

    tutorial::Person_PhoneNumber *phone = 0;
    // 添加Phone-1
    phone = person->add_phone();
    phone->set_number("1581310411");
    phone->set_type(tutorial::Person_PhoneType_MOBILE);
    
    // 添加Phone-2
    phone = person->add_phone();
    phone->set_number("1581310412");
}

int main()
{
    // 校验版本
    GOOGLE_PROTOBUF_VERIFY_VERSION; 
    tutorial::AddressBook addressbook;

    // 设置外观
    tutorial::FaceStyle *facestyle = addressbook.mutable_style();
    facestyle->set_name("test");

    tutorial::Person *person = 0;
    // 添加Person-1
    person = addressbook.add_person();
    FillPerson(person, "p1", 1, "p1@letv.com");

    // 添加Person-2
    person = addressbook.add_person();
    FillPerson(person, "p2", 2, "p2@letv.com");

    // 写文件
    fstream output("addressbook.bin", ios::out|ios::trunc|ios::binary);
    addressbook.SerializeToOstream(&output);

    // Optional:  Delete all global objects allocated by libprotobuf.
    google::protobuf::ShutdownProtobufLibrary();
    return 0;
}
