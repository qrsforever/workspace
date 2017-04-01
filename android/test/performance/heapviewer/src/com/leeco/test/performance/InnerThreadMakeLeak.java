package com.leeco.test.performance;

import android.app.Activity;
import android.os.Bundle;
import android.os.SystemClock;
import android.util.Log;

public class InnerThreadMakeLeak extends Activity {

    public static final String TAG = InnerThreadMakeLeak.class.getSimpleName();
    
    @SuppressWarnings("unused")
    private Byte[] mBigData_o = null;

    @SuppressWarnings("unused")
    private boolean[] mBigData_b = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Log.d(TAG, "onCreate");
        setContentView(R.layout.inner_thread); 

        mBigData_o = new Byte[3 * 1024 * 1024]; // 4-byte array: Total Size增长， 3MB × 4 = 12MB
        mBigData_b = new boolean[3 * 1024 * 1024]; // 1-byte array: Total Size增长， 3MB × 1 = 3MB

        // 匿名内部类Runnable含有InnerThreadMakeLeak.this, 导致不能销毁
        new Thread(new Runnable() {
            @Override
            public void run() {
                while (true) {
                    Log.d(TAG, "[" + Thread.currentThread().getName() + "] I am live");
                    SystemClock.sleep(5000);
                }
            }
        }).start();
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        Log.d(TAG, "onDestroy");

        // 正确做法将对象变量赋值null， 显示释放
        // mBigData_o = null; 
        // mBigData_b = null;
    }

}
