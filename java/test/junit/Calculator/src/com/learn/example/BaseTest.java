package com.learn.example;

import org.junit.After;
import org.junit.Before;

public class BaseTest {
    @Before
    public void setUp() throws Exception {
        System.out.println("------------------------------setup-----------------------------");
    }

    @After
    public void tearDown() throws Exception {
        System.out.println("----------------------------------------------------------------\n");
    }
}
