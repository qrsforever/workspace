package com.leeco.test;

import android.app.Activity;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.os.Message;
import android.util.Log;
import android.view.KeyEvent;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;

public class InputTimeoutActivity extends Activity {
    public static final String TAG = "InputTimeoutActivity";
    private MainHandler mHandler = null;
    private Button mB1 = null;
    @SuppressWarnings("unused")
    private Button mB2 = null;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        mB1 = (Button) this.findViewById(R.id.b1);
        mB2 = (Button) this.findViewById(R.id.b2);
        mB1.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
                // TODO Auto-generated method stub
                try {
                    Log.d(TAG, "sleep 20s");
                    Thread.sleep(20000);
                } catch (InterruptedException e){
                    e.printStackTrace();
                }
            }
        });
    }

    @Override
    protected void onResume() {
        // TODO Auto-generated method stub
        super.onResume();
        Looper looper;
        if ((looper = Looper.myLooper()) != null ||
            (looper = Looper.getMainLooper()) != null) {
            mHandler = new MainHandler(looper);
        } else {
            Log.d(TAG, "error!");
        }
        mHandler.sendEmptyMessageDelayed(0, 5000);
    }

    class MainHandler extends Handler {
        public MainHandler(Looper looper) {
            super(looper);
        }
    
        @Override
        public void handleMessage(Message msg) {
            Log.d(TAG, "get msg: " + msg.what);
            switch (msg.what) {
                case 0:
                    // try {
                        // Thread.sleep(20000);
                    // } catch (InterruptedException e){
                        // e.printStackTrace();
                    // }
                    break;
                default:
                    ;
            }
            super.handleMessage(msg);
        }
    }

    @Override
    public boolean onKeyDown(int keyCode, KeyEvent event) {
        Log.d(TAG, "onKeyDown");
        return super.onKeyDown(keyCode, event);
    }

    @Override
    public boolean onKeyUp(int keyCode, KeyEvent event) {
        Log.d(TAG, "onKeyUp");
        return super.onKeyUp(keyCode, event);
    }

}
