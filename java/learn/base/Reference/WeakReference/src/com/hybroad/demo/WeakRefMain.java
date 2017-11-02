package com.hybroad.demo;
import java.lang.ref.WeakReference;

public class WeakRefMain {
    public static void main(String[] args) {
        Student stu = new Student("Michael", 22);
        WeakReference<Student> refStu = new WeakReference<Student>(stu);
        int i = 0;
        while(true) {
            if (refStu.get() != null) {
                i++;
                System.out.println("Object is alive for " + i + "loops - " + refStu);
            } else {
                System.out.println("Object has been collected!");
                break;
            }
        }
    }
}
