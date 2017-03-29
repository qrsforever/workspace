package com.learn.example;

import org.junit.runner.Description;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;
import org.junit.runner.notification.RunListener;

public class RunnerMain {
    public static void main(String[] args) {
        Logger.d("---------------------------Start-------------------------------");
        JUnitCore core = new JUnitCore();
        core.addListener(new RunListener() {
            @Override
            public void testIgnored(Description description) throws Exception {
                if (null != description.getMethodName()) {
                    System.out.println(description.getMethodName() +  " --> Ignore\n");
                }
                super.testIgnored(description);
            }
        });
        Result result = core.run(SuiteTest.class, TheoriesTest.class, AssumeTest.class);
        for (Failure failure : result.getFailures()) {
            System.out.println(failure.toString());
        }
        if (result.wasSuccessful()) {
            System.out.println("Successfull");
        }
        Logger.d("---------------------------End---------------------------------");
    }
}
