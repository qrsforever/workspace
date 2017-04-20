package com.learn.example;

import org.junit.Rule;
import org.junit.Test;
import org.junit.experimental.categories.Category;
import org.junit.rules.TestRule;
import org.junit.runner.Description;
import org.junit.runners.model.Statement;

// Must exist one test method at least.

@Category(FastTests.class)
public class RuleTest extends BaseTest {
    public void beforeRule() {
        Logger.d("");
    }

    public void afterRule() {
        Logger.d("");
    }

    @Test
    public void testRule() {
        Logger.d("");
    }

    @Rule
    public TestRule clsRule = new TestRule() {
        @Override
        public Statement apply(Statement base, Description descr) {
            return new Statement() {
                @Override
                public void evaluate() throws Throwable {
                    beforeRule();
                    try {
                        base.evaluate();
                    } finally {
                        afterRule();
                    }
                }
            };
        }
    };
}
