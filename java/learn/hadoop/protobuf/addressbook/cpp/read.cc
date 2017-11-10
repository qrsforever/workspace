#include <iostream>
#include <fstream>
#include "addressbook.pb.h"
#include "facestyle.pb.h"

using namespace std;

void ListPerson(tutorial::AddressBook& addressbook)
{
    for (int i = 0; i < addressbook.person_size(); ++i) {
        const tutorial::Person &person = addressbook.person(i);
        cout << "Name: " << person.name() << endl;
        cout << "Id: " << person.id() << endl;
        cout << "Email: " << person.email() << endl;
        // phones
        for (int j = 0; j < person.phone_size(); ++j) {
            const tutorial::Person_PhoneNumber &phone = person.phone(j);
            cout << "\tPhone number: " << phone.number() << endl;
            cout << "\tPhone type: " << phone.type() << endl;
        }
    }
}

int main()
{
    // 校验版本
    GOOGLE_PROTOBUF_VERIFY_VERSION;
    tutorial::AddressBook addressbook;

    fstream input("addressbook.bin", ios::in|ios::binary);
    if (!addressbook.ParseFromIstream(&input)) {
        cerr << "Fail ParseFromIstream" << endl;
    }

    // 外观
    const tutorial::FaceStyle &facestyle = addressbook.style();
    cout << "FaceStyle: " << facestyle.name() << endl;

    // 迭代显示Person
    ListPerson(addressbook);

    // Optional:  Delete all global objects allocated by libprotobuf.
    google::protobuf::ShutdownProtobufLibrary();
    return 0;
}
