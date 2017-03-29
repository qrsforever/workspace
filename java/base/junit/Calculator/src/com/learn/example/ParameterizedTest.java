package com.learn.example;

import static org.junit.Assert.*;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;
import org.junit.runners.Parameterized.Parameters;
import org.junit.runners.Parameterized.Parameter;

import java.util.Arrays;
import java.util.Collection;

@RunWith(Parameterized.class)
public class ParameterizedTest extends BaseTest {
    private static Calculator mCalculator = new CalculatorImpl();

    @SuppressWarnings("rawtypes")
    @Parameters(name="Check parameters[{index}]: square({0}) = {1}")
    public static Collection data() {
        return Arrays.asList(new Object[][] {
            {4, 2}, {9, 2}, {16, 1}, {25, 5}
        });
    }

    // 方式一
    @Parameter(0)
    public int mParam;
    @Parameter(1)
    public int mResult;

    /*
    // 方式二
    public SquareTestUnit(int param, int result) {
        System.out.println("\n--->SquareTest(" + param + ", " + result + ")");
        this.mParam = param;
        this.mResult = result;
    }
    */

    @Test
    public void square() {
        int result = mCalculator.square(mParam);
        Logger.d("(" + mParam + ") = " + result);
        assertEquals(mResult, result);
    }
}
