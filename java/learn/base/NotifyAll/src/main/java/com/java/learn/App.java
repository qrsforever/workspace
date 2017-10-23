package com.java.learn;

import java.util.ArrayList;

public class App {
    ArrayList<Object> mObjs = new ArrayList<Object>();

    class Productor extends Thread {

        @Override
        public void run() {
            // notify: 只唤醒一个线程
            // notifyall: 唤醒所有线程
            while (true) {
                try {
                    Thread.sleep(1000);
                    System.out.println("Add new object");    
                    synchronized(mObjs) {
                        mObjs.add(new Object());
                        mObjs.notify();  // 必须在mObjs锁里面, 否则java.lang.IllegalMonitorStateException
                        // mObjs.notifyAll();  // 必须在mObjs锁里面, 否则java.lang.IllegalMonitorStateException
                    }
                } catch (InterruptedException e){
                    e.printStackTrace();
                }
            }
        }
    }

    class Consumer extends Thread {

        String mName = null;

        /**
         *  name: String 
         */
        public Consumer(String name) {
            super();
            mName = name;
        }

        @Override
        public void run() {
            synchronized(mObjs) {
                try {
                    System.out.println("Thread[" + mName + "] wait");
                    mObjs.wait();
                    if (mObjs.size() != 0) {
                        System.out.println("Thread[" + mName + "] remove");
                        mObjs.remove(0);
                    } else {
                        System.out.println("Thread[" + mName + "]: no objs");
                    }
                } catch(Exception e){
                    e.printStackTrace();
                }
            }
        } 
    }

    public static void main(String[] args) {
        App app = new App();
        Productor p1 = app.new Productor();
        p1.start();
        for(int i = 0; i < 10; ++i) {
            app.new Consumer("c" + i).start();
        }

        while (true)
            ;
    }
}
