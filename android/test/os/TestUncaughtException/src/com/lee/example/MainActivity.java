package com.lee.example;

import android.app.Activity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.os.Process;

public class MainActivity extends Activity
{
    private static final String TAG = "MainActivity";

    private static class UncaughtHandler implements Thread.UncaughtExceptionHandler {
        public void uncaughtException(Thread t, Throwable e) {
            Log.d(TAG, " uncaughtException ");
            try {
                throw e;
            } catch (Throwable e1) {
                // TODO Auto-generated catch block
                e1.printStackTrace();
            }
            // Process.killProcess(Process.myPid());
            // System.exit(10);
        }
    }

    @Override
    public void onCreate(Bundle savedInstanceState)
    {
        Log.d(TAG, "onCreate");
        Thread.setDefaultUncaughtExceptionHandler(new UncaughtHandler());

        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
    }

    public void onHit(View view) 
    {
        Log.d(TAG, "onHit");
        Button button = null; // null pointer exception
        button.setVisibility(View.VISIBLE);
    }
}
