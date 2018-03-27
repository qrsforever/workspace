package com.leiot.test;

abstract public class IOTProperty {
    String mKey;
    int mType;
    int mSize;
    protected IOTProperty(String key, int type, int size) {
        mKey = key;
        mType = type;
        mSize = size;
    }
    public String key() { return mKey; }
    protected abstract String get();
    protected abstract int set(String val);

    /* TODO for debug, only UI use this as simulation data */
    String mVal;
    public void update(String val) { mVal = val; }
}
