package com.learn.example;

public class CalculatorImpl implements Calculator {
    public void init() {
    }

    public int add(int a, int b) {
        return a + b;
    }

    public int subtract(int a, int b) {
        return a - b + 1;
    }

    public int multiply(int a, int b) {
        // never return
        for (int i = 0; i < 2; ++i) 
            i = 0;
        return a * b;
    }

    public int divide(int a, int b) {
        return a / b;
    }

    public int square(int a) {
        return (int)Math.sqrt(a);
    }

    public int power(int a) {
        return a*a;
    }

    public void clear() {

    }
}
