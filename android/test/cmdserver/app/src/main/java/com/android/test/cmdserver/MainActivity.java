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
    static final String TAG = "QRS-MainActivity";
    CommandService mService;
    MyReceiver mReceiver;
    Button mBtnStart, mBtnStop;
    TextView mTxt;
    Intent mIntent;
    private MyApplication myApplication;

    public static boolean isServiceRunning(Context context, String ServiceName) {
        if (TextUtils.isEmpty(ServiceName))
            return false;
        ActivityManager myManager = (ActivityManager)context.getSystemService(Context.ACTIVITY_SERVICE);
        ArrayList<ActivityManager.RunningServiceInfo> runningService =
            (ArrayList<ActivityManager.RunningServiceInfo>)myManager.getRunningServices(80);
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

        mBtnStart = (Button)findViewById(R.id.start);
        mBtnStart.setTag(Constants.CMD_START_SERVICE);
        mBtnStart.setOnClickListener(new onButtonClickListener());
        mBtnStop = (Button)findViewById(R.id.stop);
        mBtnStop.setTag(Constants.CMD_STOP_SERVICE);
        mBtnStop.setOnClickListener(new onButtonClickListener());
        mIntent = new Intent(MainActivity.this, CommandService.class);
        mBtnStart.setEnabled(false);
        mBtnStop.setEnabled(false);
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
        boolean running = isServiceRunning(this, "com.android.test.cmdserver.CommandService");
        if (!running) {
            mTxt.setText("StartService...");
            Log.i(TAG, "startService :" + running);
            startService(mIntent);
        } else {
            mTxt.setText("Service is running!");
            mBtnStart.setEnabled(false);
            mBtnStop.setEnabled(true);
        }
        mReceiver = new MyReceiver(mTxt);
        IntentFilter mFilter= new IntentFilter();
        mFilter.addAction("android.intent.action.cmdactivity");
        MainActivity.this.registerReceiver(mReceiver, mFilter);
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        Log.i(TAG, "onDestroy");
        // mySendBroadcast(Constants.CMD_STOP_SERVICE, 0);
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

                switch (cmd) {
                    case Constants.CMD_SHOW_INFO:
                        mInfo.setText(bundle.getString("str"));
                        break;
                    case Constants.CMD_SHOW_TOAST:
                        myShowToast(bundle.getString("str"));
                        break;
                    case Constants.CMD_LUALU_RUNNING:
                        Log.d(TAG, "RUNNING");
                        mBtnStart.setEnabled(false);
                        mBtnStop.setEnabled(true);
                        mTxt.setText("Service is running!");
                        break;
                    case Constants.CMD_LUALU_QUIT:
                        Log.d(TAG, "QUIT");
                        mTxt.setText("薅羊毛");
                        mBtnStart.setEnabled(true);
                        mBtnStop.setEnabled(false);
                        break;
                    case Constants.CMD_SYSTEM_EXIT:
                        System.exit(0);
                        break;
                    default:
                        ;
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
        Log.d(TAG, "sendBroadcast: " + Constants.CMD_SEND_DATA + " " + value);
    }

    /*
     * Handle click event
     */
    public class onButtonClickListener implements OnClickListener{
        @Override
        public void onClick(View v) {
            // send broadcast
            // int cmd = Constants.CMD_SEND_DATA;
            int value = (Integer)v.getTag();
            switch (value) {
                case Constants.CMD_START_SERVICE:
                    Intent intent = new Intent(MainActivity.this, CommandService.class);
                    // boolean running = isServiceRunning(MainActivity.this, "com.android.test.cmdserver.CommandService");
                    // if (!running) {
                        // Log.i(TAG, "startService :" + running);
                        startService(intent);
                    // }
                    break;
                case Constants.CMD_STOP_SERVICE:
                    mySendBroadcast(Constants.CMD_STOP_SERVICE, 0);
                    break;
                default:
                    ;
            }
        }
    }
}
