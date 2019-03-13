package com.android.test.cmdserver;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.content.BroadcastReceiver;
import android.content.IntentFilter;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;
import java.util.ArrayList;
import android.app.ActivityManager;
import android.text.TextUtils;

public class MainActivity extends Activity {
    protected String TAG = "MainActivity";
    CommandService mService;
    MyReceiver mReceiver;
    // Button mBtnStart, mBtnStop;
    TextView mTxt;
    Intent mIntent;
    private MyApplication myApplication;

    /* Define activity command */
    static final int CMD_START_SERVICE = 0x00;
    static final int CMD_STOP_SERVICE = 0x01;
    static final int CMD_SYSTEM_EXIT  = 0x02;
    static final int CMD_SHOW_TOAST   = 0x03;
    static final int CMD_SEND_DATA    = 0x04;
    static final int CMD_SHOW_INFO    = 0x05;

    public static boolean isServiceRunning(Context context, String ServiceName) {
        if (TextUtils.isEmpty(ServiceName))
            return false;
        ActivityManager myManager = (ActivityManager)context.getSystemService(Context.ACTIVITY_SERVICE);
        ArrayList<ActivityManager.RunningServiceInfo> runningService =
            (ArrayList<ActivityManager.RunningServiceInfo>)myManager.getRunningServices(30);
        for (int i = 0; i < runningService.size(); i++) {
            if (runningService.get(i).service.getClassName().toString().equals(ServiceName))
                return true;
        }
        return false;
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        myApplication = new MyApplication();
        myApplication.addActivity(this);

        mTxt = (TextView)findViewById(R.id.showInfo);

        // mBtnStart = (Button)findViewById(R.id.start);
        // mBtnStart.setTag(CMD_START_SERVICE);
        // mBtnStart.setOnClickListener(new onButtonClickListener());
        // mBtnStop = (Button)findViewById(R.id.stop);
        // mBtnStop.setTag(CMD_STOP_SERVICE);
        // mBtnStop.setOnClickListener(new onButtonClickListener());
        mIntent = new Intent(MainActivity.this, CommandService.class);
        boolean running = isServiceRunning(this, "com.android.test.cmdserver.CommandService");
        if (!running) {
            mTxt.setText("StartService...");
            Log.i(TAG, "startService :" + running);
            startService(mIntent);
        } else {
            // mBtnStart.setEnabled(false);
            // mBtnStop.setEnabled(true);
        }
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();
        if (id == R.id.action_settings) {
            return true;
        }
        return super.onOptionsItemSelected(item);
    }

    @Override
    protected void onResume() {
        super.onResume();
        Log.i(TAG, "onResume");
        mReceiver = new MyReceiver(mTxt);
        IntentFilter mFilter= new IntentFilter();
        mFilter.addAction("android.intent.action.cmdactivity");
        MainActivity.this.registerReceiver(mReceiver, mFilter);
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        Log.i(TAG, "onDestroy");
        mySendBroadcast(CMD_STOP_SERVICE, 0);
        if ( mReceiver != null ) {
            MainActivity.this.unregisterReceiver(mReceiver);
        }
        myApplication.removeActivity(this);
    }

    /*
     * BroadcastReceiver for Service
     */
    public class MyReceiver extends BroadcastReceiver {

        public TextView mInfo;
        public MyReceiver(TextView txt) {
            mInfo = txt;
        }
        @Override
        public void onReceive(Context context, Intent intent) {
            if(intent.getAction().equals("android.intent.action.cmdactivity")){
                Bundle bundle = intent.getExtras();
                int cmd = bundle.getInt("cmd");

                if (cmd == CMD_SHOW_TOAST) {
                    myShowToast(bundle.getString("str"));
                } else if (cmd == CMD_SYSTEM_EXIT) {
                    System.exit(0);
                } else if (cmd == CMD_SHOW_INFO) {
                    mInfo.setText(bundle.getString("str"));
                }
            }
        }
    }

    /*
     * Show message on screen
     */
    public void myShowToast(String str) {
        Toast.makeText(getApplicationContext(), str, Toast.LENGTH_SHORT).show();
    }

    /*
     * Send message to service
     */
    public void mySendBroadcast(int cmd, int value) {
        Intent intent = new Intent();
        intent.setAction("android.intent.action.cmdservice");
        intent.putExtra("cmd", cmd);
        intent.putExtra("value", value);
        sendBroadcast(intent);
        Log.d(TAG, "sendBroadcast: " + CMD_SEND_DATA + " " + value);
    }

    /*
     * Handle click event
     */
    public class onButtonClickListener implements OnClickListener{
        @Override
        public void onClick(View v) {
            // send broadcast
            int cmd = CMD_SEND_DATA;
            int value = (Integer)v.getTag();
            switch (value) {
                case CMD_START_SERVICE:
                    Intent intent = new Intent(MainActivity.this, CommandService.class);
                    boolean running = isServiceRunning(MainActivity.this, "com.android.test.cmdserver.CommandService");
                    if (!running) {
                        Log.i(TAG, "startService :" + running);
                        startService(intent);
                    }
                    break;
                case CMD_STOP_SERVICE:
                    mySendBroadcast(cmd, value);
                    break;
                default:
                    ;
            }
        }
    }
}
