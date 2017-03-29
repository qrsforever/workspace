package com.learn.example;

import org.junit.Ignore;
import org.junit.Test;

@Ignore("Ignore annotation!")
public class IgnoredTest {
    @Test
    public void testIgnore() {
        Logger.d("Never run here!");
    }
}
