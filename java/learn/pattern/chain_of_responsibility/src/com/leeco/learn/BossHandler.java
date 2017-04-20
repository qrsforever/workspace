package com.leeco.learn;

public class BossHandler extends Handler {

    @Override
    public boolean handlerMessage(int what) {
        System.out.println("Boss can do it!");
        return true;
    }
    
}
