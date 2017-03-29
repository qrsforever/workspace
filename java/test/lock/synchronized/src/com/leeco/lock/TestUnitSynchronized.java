package com.leeco.lock;

import static org.junit.Assert.*;
import org.junit.Test;

public class TestUnitSynchronized {
    private Object mO = new Object();
    private static int mNum = 0;
    private static int mNum2 = 0;

    @Test(timeout=100)
    public void testSyncInOneThread() {
        synchronized(mO) {
            System.out.println("testSyncInOneThread 1");
            synchronized(mO) {
                System.out.println("testSyncInOneThread 2");
            }
        } 
        synchronized(this) {
            System.out.println("testSyncInOneThread 3");
            synchronized(this) {
                System.out.println("testSyncInOneThread 4");
            }
        }
        assertEquals(0, 0);
    }

    public class NamedRunnable implements Runnable {
        protected String mName = "";

        public NamedRunnable(String name) {
            mName = name;
        }

        @Override
        public void run() {
            doInBackground(mName);
        }
    }

    public class NamedRunnable2 extends NamedRunnable {

        public NamedRunnable2(String name) {
            super(name);
        }

        @Override
        public void run() {
            System.out.println(" NamedRunnable2 run in " + super.mName);
            synchronized(mO) {
                System.out.println("NamedRunnable2 " + mNum2);
                mNum2++;
                letwait(0x1ffffff);
            }
            System.out.println(" NamedRunnable2 run out " + super.mName);
        }
    }

    private void letwait(long cnt) {
        @SuppressWarnings("unused")
        long nouseful = 0;
        for (long i = 0; i < cnt; i++)
            nouseful += 1;
    }

    private void doInBackground(String name) {
        System.out.println(" doInBackground in " + name);
        synchronized(mO) {
            System.out.println("NamedRunnable " + mNum);
            mNum++;
            letwait(0x1ffffff);
        }
        System.out.println(" doInBackground out " + name);
    }

    @Test
    public void testSyncInMultiThread() {
        mNum = 0;
        new Thread(new NamedRunnable("1")).start();
        new Thread(new NamedRunnable("2")).start();
        new Thread(new NamedRunnable("3")).start();
        letwait(0x3ffffff);
        assertTrue(3 != mNum);
    }

    @Test
    public void testSyncInMultiThread2() {
        mNum2 = 0;
        new Thread(new NamedRunnable2("4")).start();
        new Thread(new NamedRunnable2("5")).start();
        new Thread(new NamedRunnable2("6")).start();
        letwait(0x3ffffff);
        assertTrue(3 != mNum2);
    }
}

// 验证同一个线程相同对象锁没有问题
