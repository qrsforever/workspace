package com.learn.example;

public final class Logger {
    public static void d(String msg) {                                         
        StackTraceElement s = new Throwable().getStackTrace()[1];
        System.out.println("Log:" + 
                s.getClassName().split("\\.")[3] + ".java:" +
                s.getLineNumber() + " " + 
                s.getMethodName() + ":" + msg); 
    }
}
