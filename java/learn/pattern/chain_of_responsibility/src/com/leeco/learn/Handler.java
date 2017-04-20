package com.leeco.learn;

public abstract class Handler {
    protected Handler mH = null;
    protected static int eLevel_Employee = 0;
    protected static int eLevel_Captain = 1;
    protected static int eLevel_Chief = 2;
    protected static int eLevel_Boss = 3;

    public void setSuccessor(Handler handler) {
        mH = handler;
    }
    public Handler getSuccessor() {
        return mH;
    }

    public abstract boolean handlerMessage(int what);
}
