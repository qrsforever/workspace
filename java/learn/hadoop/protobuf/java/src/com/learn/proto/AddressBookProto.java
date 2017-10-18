package com.learn.proto;

import java.io.FileOutputStream;
import java.io.FileInputStream;

import com.google.protobuf.InvalidProtocolBufferException;

import com.learn.proto.Facestyle.FaceStyle;
import com.learn.proto.OuterAddressBook.AddressBook;
import com.learn.proto.OuterAddressBook.Person;
import com.learn.proto.OuterAddressBook.Person.PhoneNumber;

public class AddressBookProto {

    static private Person FillPerson(String name, int id, String email) {
        Person.Builder person = Person.newBuilder();
        person.setName(name);
        person.setId(id);
        person.setEmail(email);

        PhoneNumber.Builder phone = null;
        // 添加Phone-1
        phone = PhoneNumber.newBuilder();
        phone.setNumber("1581310411");
        phone.setType(Person.PhoneType.MOBILE);
        person.addPhone(phone.build());

        // 添加Phone-2
        phone = PhoneNumber.newBuilder();
        phone.setNumber("1581310412");
        person.addPhone(phone.build());

        return person.build();
    }

    static private void ListPerson(AddressBook addressbook){
        for (Person person : addressbook.getPersonList()) {
            System.out.println("Name: " + person.getName());
            System.out.println("Id: " + person.getId());
            System.out.println("Email: " + person.getEmail());

            for(PhoneNumber phone : person.getPhoneList()) {
                System.out.println("   PhoneNumber: " + phone.getNumber());
                System.out.println("   PhoneType: " + phone.getType());
            }
        }
    }

    public static void main(String[] args) throws Exception{
        // 外观
        FaceStyle.Builder facestyle = FaceStyle.newBuilder();
        facestyle.setName("test");

        AddressBook.Builder addressbook = AddressBook.newBuilder();
        addressbook.setStyle(facestyle.build());

        // 添加Person-1
        addressbook.addPerson(FillPerson("p1", 1, "p1@letv.com"));

        // 添加Person-2
        addressbook.addPerson(FillPerson("p2", 2, "p2@letv.com"));

        FileOutputStream output = new FileOutputStream("addressbook.bin");
        addressbook.build().writeTo(output);
        output.close();

        // 反序列化
        AddressBook ab = AddressBook.parseFrom(new FileInputStream("addressbook.bin"));
        System.out.println("Facestyle: " + ab.getStyle().getName());
        ListPerson(ab);
    }
}
