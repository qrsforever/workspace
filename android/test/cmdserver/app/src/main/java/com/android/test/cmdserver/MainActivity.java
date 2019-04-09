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
import android.widget.CompoundButton;
import android.widget.CompoundButton.OnCheckedChangeListener;
import android.widget.Switch;
import java.util.ArrayList;
import android.app.ActivityManager;
import android.text.TextUtils;
import android.os.Build;
import java.lang.reflect.Method;

public class MainActivity extends Activity implements OnCheckedChangeListener {
    static final String TAG = "QRS-MainActivity";
    CommandService mService;
    MyReceiver mReceiver = null;
    Button mBtnStart, mBtnStop;
    Switch mSwHui, mSwQu, mSwDuo;
    TextView mTxt;
    private MyApplication myApplication;
    int mSwitchVals[] = { 1, 1, 1 };


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        myApplication = new MyApplication();
        myApplication.addActivity(this);

        mTxt = (TextView)findViewById(R.id.showInfo);

        mSwQu  = (Switch)findViewById(R.id.qutoutiao_sw);
        mSwHui = (Switch)findViewById(R.id.huitoutiao_sw);
        mSwDuo = (Switch)findViewById(R.id.toutiaoduoduo_sw);

        mSwQu.setOnCheckedChangeListener(this);
        mSwHui.setOnCheckedChangeListener(this);
        mSwDuo.setOnCheckedChangeListener(this);

        mBtnStart = (Button)findViewById(R.id.start);
        // mBtnStart.setTag(Constants.CMD_START_SERVICE);
        mBtnStart.setOnClickListener(new onButtonClickListener());
        mBtnStop = (Button)findViewById(R.id.stop);
        // mBtnStop.setTag(Constants.CMD_STOP_SERVICE);
        mBtnStop.setOnClickListener(new onButtonClickListener());
    }

    @Override
    public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
        int flg = 0;
        switch (buttonView.getId()) {
            case R.id.huitoutiao_sw:
                flg = 0;
                break;
            case R.id.qutoutiao_sw:
                flg = 1;
                break;
            case R.id.toutiaoduoduo_sw:
                flg = 2;
                break;
            default:
                return;
        }
        if (isChecked) {
            mSwitchVals[flg] = 1;
        } else {
            mSwitchVals[flg] = 0;
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
        boolean running = Utils.isServiceRunning(this, "com.android.test.cmdserver.CommandService");
        if (running) {
            mTxt.setText("正在努力薅羊毛..");
            mBtnStart.setEnabled(false);
            mBtnStop.setEnabled(true);
        } else {
            if (Build.PRODUCT.equals("LeMax2_CN")) {
                String value = Utils.getProperty("init.svc.letv_fts_service");
                if ("running".equals(value))
                    Utils.setProperty("ctl.stop", "letv_fts_service");
            }
            mBtnStart.setEnabled(true);
            mBtnStop.setEnabled(false);
        }
        if (mReceiver == null) {
            mReceiver = new MyReceiver(mTxt);
            IntentFilter mFilter= new IntentFilter();
            mFilter.addAction("android.intent.action.cmdactivity");
            MainActivity.this.registerReceiver(mReceiver, mFilter);
        }
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        Log.i(TAG, "onDestroy");
        // mySendBroadcast(Constants.CMD_STOP_SERVICE, 0);
        if ( mReceiver != null ) {
            MainActivity.this.unregisterReceiver(mReceiver);
        }
        mReceiver = null;
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
                        mTxt.setText("正在努力薅羊毛..");
                        break;
                    case Constants.CMD_LUALU_QUIT:
                        Log.d(TAG, "QUIT");
                        mTxt.setText("继续薅羊毛");
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
            Log.d(TAG, "on click: " + v.getId());
            // send broadcast
            // int cmd = Constants.CMD_SEND_DATA;
            // int value = (Integer)v.getTag();
            switch (v.getId()) {
                case R.id.start:
                    Intent intent = new Intent(MainActivity.this, CommandService.class);
                    StringBuilder sb = new StringBuilder();
                    sb.append(String.valueOf(mSwitchVals[0])).append(" ");
                    sb.append(String.valueOf(mSwitchVals[1])).append(" ");
                    sb.append(String.valueOf(mSwitchVals[2])).append(" ");
                    intent.putExtra("args", sb.toString());
                    Log.d(TAG, "start");
                    startService(intent);
                    break;
                case R.id.stop:
                    Intent intent2 = new Intent();
                    intent2.setAction("android.intent.action.cmdservice");
                    intent2.putExtra("cmd", Constants.CMD_STOP_SERVICE);
                    Log.d(TAG, "stop");
                    sendBroadcast(intent2);
                    break;
                default:
                    ;
            }
        }
    }
}
