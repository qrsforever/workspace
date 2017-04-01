package com.leeco.test.performance;

import java.lang.ref.WeakReference;

import android.app.Activity;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.util.Log;

public class HandlerClassMakeLeak extends Activity {

    public static final String TAG = HandlerClassMakeLeak.class.getSimpleName();

    private MyHandler mHandler = new MyHandler();
    private final QQHandler mQQ = new QQHandler(this);

    @SuppressWarnings("unused")
    private int[] mBigData_i = new int[3 * 1024 * 1024]; // 验证Activity没有GC掉

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        // TODO Auto-generated method stub
        super.onCreate(savedInstanceState);
        setContentView(R.layout.handler_class);
        
        // 将消息发送到主线程10s后处理， 期间Activity不能被GC
        // mHandler.sendEmptyMessageDelayed(0, 10000);
        mQQ.sendEmptyMessageDelayed(0, 10000);
    }

    // 非静态类含有外部类的引用
    class MyHandler extends Handler {
        @Override
        public void handleMessage(Message msg) {
            Log.d(TAG, "Get msg.what = " + msg.what);
            switch (msg.what) {
            }
            super.handleMessage(msg);
        }
    }

    // 正确的写法
    public static class QQHandler extends Handler {

        private final WeakReference<HandlerClassMakeLeak> mWeakContext;

        public QQHandler(HandlerClassMakeLeak context) {
            super();
            mWeakContext = new WeakReference<HandlerClassMakeLeak>(context);
        }

        @Override
        public void handleMessage(Message msg) {
            Log.d(TAG, "Get msg.what = " + msg.what);
            switch (msg.what) {
                case 0:
                    if (mWeakContext.get() != null) {

                    } else {
                        Log.d(TAG, "GC: Sorry!");
                    }
                    break;
            }
            super.handleMessage(msg);
        }
    }


}
