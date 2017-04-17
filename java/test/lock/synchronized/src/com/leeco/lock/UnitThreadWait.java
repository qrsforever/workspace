package com.leeco.lock;

import static org.junit.Assert.*;
import org.junit.Test;

public class UnitThreadWait {

    public void doInThread() {
        synchronized(this) {
            try {
                System.out.println("wait");
                this.wait(); // 释放对象锁
            } catch(Exception e){
                e.printStackTrace();
            }
        }
    }

    @Test
    public void mainThreadWaitWillReleaseLock() {
        new Thread(new Runnable() {
            @Override
            public void run() {
                doInThread();
            }
        }).start();

        new Thread(new Runnable() {
            @Override
            public void run() {
                doInThread();
            }
        }).start();

        try {
            Thread.sleep(10000);
        } catch (InterruptedException e){
            e.printStackTrace();
        }
    }

}
