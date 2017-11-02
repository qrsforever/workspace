package com.hybroad.demo;

public class Student {
    private String _name;
    private int _age;
    public Student(String name, int age) {
        _name = name;
        _age = age;
    }
    public String getName() {
        return _name;
    }
    public int getAge() {
        return _age;
    }
}

