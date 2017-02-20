package com.hybroad.demo.looper;

import android.app.Activity;
import android.os.Bundle;
import android.os.Handler;
import android.os.HandlerThread;
import android.os.Looper;
import android.os.Message;
import android.util.Log;

public class LooperDemoActivity extends Activity {
    /** Called when the activity is first created. */
    private static final String TAG = "Hybroad-LooperDemoActivity";
    private static final int CMD_LOG = 1;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        Log.d(TAG, "Main threadID: " + Thread.currentThread().getId());

        // 1. 在主线程中
        new Handler().post(new Runnable() {
            @Override
            public void run() {
                try {
                    Thread.sleep(2000);
                } catch (Exception e) {
                    e.printStackTrace();
                }
                Log.d(TAG, "Handler-1 threadID: " + Thread.currentThread().getId());
            }
        });

        // 2. 在Handler线程中
        final HandlerThread handler = new HandlerThread("Handler-2");
        handler.start();
        new Handler(handler.getLooper()).postDelayed(new Runnable() {
            @Override
            public void run() {
                Log.d(TAG, handler.getName() + " threadID: " + Thread.currentThread().getId());
            }
        }, 1000);

        // 3. 自己实现Handler线程
        MyHandlerThread myTask = new MyHandlerThread("Handler-3");
        // myTask.start();
        myTask.exec(CMD_LOG);
    }

    private class MyHandlerThread extends Thread {
        private Handler mHandler;
        public MyHandlerThread(String name) {
            super(name);
            start();
        }
        @Override
        public void run() {
            Looper.prepare();        
            // 在此线程中创建的Handler发送的消息会到本线程的消息队列
            mHandler = new Handler() {
                public void handleMessage(Message msg) {
                    switch (msg.what) {
                        case CMD_LOG:
                            Log.d(TAG, Thread.currentThread().getName() + "  threadID: " + Thread.currentThread().getId());
                            break;
                        default:
                            break;
                    }
                }
            };
            Looper.loop();
        }

        void exec(int cmd) {
            // 在主线程调用该接口, Handler对象可能在另一个对象没有创建
            while (mHandler == null) {
                try {
                    Thread.sleep(100);
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
            Log.d(TAG, Thread.currentThread().getName() + " exec threadID: " + Thread.currentThread().getId());
            // Message msg = mHandler.obtainMessage(cmd);
            // mHandler.sendMessage(msg);
            mHandler.sendEmptyMessage(cmd);
        }
    }
}
