package com.leeco.lock;

import java.io.InputStreamReader;
import java.io.Reader;
import java.io.IOException;

public class LockMain {

    // private Object o = new Object();

    private void doInThread(String name) {
        synchronized(this) {
            try {
                System.out.println("wait [" + name + "]");
                this.wait(); // 释放对象锁   (首先必须握有对象锁，即synchronized(x) then x.wait())
                System.out.println("wakeup [" + name + "]");
            } catch(Exception e){
                e.printStackTrace();
            }
        }
    }

    public class LeecoRunnable implements Runnable {
        private String mName = null;

        public LeecoRunnable(String name) {
            mName = name;
        }

        public void run() {
            doInThread(mName);
        }
    }

    public void doNotify() {
        synchronized(this) {
            try {
                this.notifyAll();  // 首先必须握有对象锁x， 在x.notifyAll
            } catch(Exception e){
                e.printStackTrace();
            }
        }
    }

    public static void main(String[] args) throws IOException {
        System.out.println("main run");
        Reader r = new InputStreamReader(System.in);
        LockMain main = new LockMain();
        System.out.println(main);
        new Thread(main.new LeecoRunnable("Thread 1")).start();    
        new Thread(main.new LeecoRunnable("Thread 2")).start();    
        new Thread(main.new LeecoRunnable("Thread 3")).start();    
        r.read();
        new Thread(new Runnable() {
            @Override
            public void run() {
                main.doNotify();
            }
        }).start();
        r.read();
    }   

}

// 总结： wait notify notifyAll 关联的是对象锁, 本实例就是LockMain.this对象。
// 弄明白对象的线程池, 哪个对象
