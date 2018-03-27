package com.leiot.test;

abstract public class IOTCommand {
    String mName;
    protected IOTCommand(String name) {
        mName = name;
    }
    public String name() { return mName; }
    protected abstract int call(String params);
}
