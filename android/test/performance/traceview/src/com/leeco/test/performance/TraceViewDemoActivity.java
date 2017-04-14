package com.leeco.test.performance;

import java.io.FileInputStream;
import java.io.InputStream;

import android.app.Activity;
import android.os.Bundle;
import android.os.Debug;
import android.os.Environment;
import android.os.Handler;
import android.os.SystemClock;
import android.util.Log;

public class TraceViewDemoActivity extends Activity {
    public static final String TAG = TraceViewDemoActivity.class.getSimpleName();

    private Handler mH = new Handler();

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

        mH.post(new Runnable() {

            @Override
            public void run() {
                Log.d(TAG, "On main thread run");
                InputStream in = null;
                byte[] tempbytes = new byte[1024];  
                int byteread = 0;
                try {
                    in = new FileInputStream(Environment.
                            getExternalStorageDirectory().getPath() + "/test.bin");  
                    while ((byteread = in.read(tempbytes)) != -1) {
                        myLog("read [" + byteread + "]");
                    }
                } catch(Exception e) {
                    e.printStackTrace();
                } finally {
                    if (in != null) {
                        try {
                            in.close();
                        } catch(Exception e){
                            e.printStackTrace();
                        }
                    }
                }
            }
        });
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
/*
I find a solution about it. Just replace the sdk_home/tools/lib/monitor-x86/plugins/com.android.ide.eclipse.traceview_24.3.3.2016344.jar  with   sdk_home/tools/lib/traveview.jar .Note that rename the file name at the same time.
 * 
 */
