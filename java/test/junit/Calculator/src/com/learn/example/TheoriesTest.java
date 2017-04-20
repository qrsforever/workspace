package com.learn.example;

import static org.junit.Assert.assertTrue;

import org.junit.experimental.theories.DataPoint;
import org.junit.experimental.theories.DataPoints;
import org.junit.experimental.theories.FromDataPoints;
import org.junit.experimental.theories.Theories;
import org.junit.experimental.theories.Theory;
import org.junit.runner.RunWith;

@RunWith(Theories.class)
public class TheoriesTest extends BaseTest {
    @DataPoints 
    public static int[] testUname = { 1, 2 }; 

    @DataPoints("arg0")
    public static int[] testDatas = { 3, 4 };  // modifier must static and public

    @DataPoints("arg1")
    public static int[] generateResults() {
        return new int[] { 9, 16 };
    }

    @DataPoint
    public static int testResult = 100;

    @Theory
    public void testShow(int param) { // will be called with every value in 'testUname' , 'testDatas' and 'testResult'
        Logger.d("(" + param + ")");
        assertTrue(param > 4); // will interrupted. other parameters will not test.
    }

    @Theory
    public void testPower(
            @FromDataPoints("arg0") int param, 
            @FromDataPoints("arg1") int result) {
        String expr = String.format("testPower(%d * %d) = %d is true ?", param, param, result);
        Logger.d(expr);
        assertTrue(param < 4 || result < 9); // 4 * 4 = 16 will not test.
    }
}
