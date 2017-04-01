package com.leeco.test.performance;

import android.app.Activity;
import android.os.Bundle;
import android.os.Debug;
import android.os.Environment;
import android.os.SystemClock;
import android.util.Log;

public class TraceViewDemoActivity extends Activity {
    public static final String TAG = TraceViewDemoActivity.class.getSimpleName();

    public TraceViewDemoActivity() {
        super();
        Log.d(TAG, "Contructor");
        // 启动采集
        Debug.startMethodTracing(Environment.
                getExternalStorageDirectory().getPath() + "/" + TAG);
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Log.d(TAG, "onCreate");
        setContentView(R.layout.main);
        new Thread(new Runnable() {
            @Override
            public void run() {
                int i = 0;
                while (i < 100) {
                    SystemClock.sleep(50);
                    ++i;
                }
            }
        }).start();
        for (int i = 0; i < 500; i++) {
            myLog("i = " + i);
        }
    }

    private void myLog(String txt) {
        Log.d(TAG, txt);
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        Log.d(TAG, "onDestroy");
    }

    @Override
    protected void onStop() {
        super.onStop();
        Log.d(TAG, "onStop");
        // 结束采集
        Debug.stopMethodTracing();
    }
}
