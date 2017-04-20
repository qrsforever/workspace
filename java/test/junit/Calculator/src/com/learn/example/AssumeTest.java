package com.learn.example;

import static org.junit.Assume.assumeTrue;

import org.junit.Before;
import org.junit.Test;

public class AssumeTest {
    private static final float VERSION = 4.12f;
    @Before
    public void setUp() throws Exception {
        Logger.d("AssumeTest setUp not past");
        assumeTrue(5.0f <= VERSION);
    }

    @Test
    public void testAssume() {
        Logger.d("Never run here!");
    }
}
