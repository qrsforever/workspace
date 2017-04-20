package com.learn.example;

import static org.junit.Assert.assertEquals;

import org.junit.Ignore;
import org.junit.Test;
import org.junit.experimental.categories.Category;

@Category(FastTests.class)
public class BlockJUnit4Test extends BaseTest {
    private static Calculator mCalculator = new CalculatorImpl();
    @Test 
    public void testAdd() { 
        Logger.d("");
        int result = mCalculator.add(1, 2);
        assertEquals(3, result);
    }

    @Test
    @Ignore("testSubtract Not yet implemented")
    public void testSubtract() {
        Logger.d("");
        int result = mCalculator.subtract(1, 2);
        assertEquals(-1, result);
    }

    @Test(timeout=200)
    public void testMultiply() {
        Logger.d("");
        int result = mCalculator.multiply(2, 3);
        assertEquals(6, result);
    }

    @Test(expected = ArithmeticException.class)
    public void testDivide() {
        Logger.d("");
        int result = mCalculator.divide(2, 0);
        assertEquals(0, result);
    }

    @Category(SlowTests.class)
    @Test
    public void testSlow() {
        Logger.d("");
    }
}
