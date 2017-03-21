package com.leeco.test;

import android.app.Activity;
import android.os.Bundle;
import android.util.Log;
import android.view.KeyEvent;

public class InputTimeoutActivity extends Activity {
    public static final String TAG = "InputTimeoutActivity";
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
    }

    @Override
    public boolean onKeyDown(int keyCode, KeyEvent event) {
        Log.d(TAG, "onKeyDown");
        // try {
            // Thread.sleep(20000);
        // } catch (InterruptedException e){
            // e.printStackTrace();
        // }
        Log.d(TAG, "onKeyDown2");
        return super.onKeyDown(keyCode, event);
    }

    @Override
    public boolean onKeyUp(int keyCode, KeyEvent event) {
        Log.d(TAG, "onKeyUp");
        // try {
            // Thread.sleep(20000);
        // } catch (InterruptedException e){
            // e.printStackTrace();
        // }
        Log.d(TAG, "onKeyUp2");
        return super.onKeyUp(keyCode, event);
    }

}
