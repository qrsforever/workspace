package com.learn.example;

import org.junit.ClassRule;
import org.junit.Test;
import org.junit.rules.ExternalResource;
import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import org.junit.runners.Suite.SuiteClasses;

// Suite Runner only test: @BeforeClass @AfterClass @ClassRule static method

@RunWith(Suite.class)
@SuiteClasses({CategoryTest.class, ParameterizedTest.class, IgnoredTest.class})
public class SuiteTest extends BaseTest {

    public static void beforeClassRule() {
        Logger.d("");
    }

    public static void afterClassRule() {
        Logger.d("");
    }
    // ExternalResource implements TestRules
    @ClassRule
    public static ExternalResource getResource() {
        return new ExternalResource() {
            @Override
            protected void before() throws Throwable {
                beforeClassRule();
                super.before();
            }
            @Override
            protected void after() {
                afterClassRule();
                super.after();
            }
        };
    }
    @Test
    public void testNull() {
        Logger.d(""); // Warning: never run here!
    }
}
