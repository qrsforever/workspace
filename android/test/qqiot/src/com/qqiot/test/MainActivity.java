package com.qqiot.test;

import android.app.Activity;
import android.os.Bundle;
import android.util.Log;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.widget.TextView;
import android.widget.EditText;
import android.widget.Button;
import android.widget.SeekBar;
import android.widget.SeekBar.OnSeekBarChangeListener;
import android.view.View;
import android.view.View.OnClickListener;

public class MainActivity extends Activity implements OnClickListener,
       OnSeekBarChangeListener {
    public static final String TAG = MainActivity.class.getSimpleName();

    IOTCloud mIot = null;
    IOTReceiver mIotReceiver = null;

    private static Button mSignalBtn = null;
    private static SeekBar mBrightnessSB = null;
    private static Button mVolUpBtn = null;
    private static Button mVolDownBtn = null;

    @Override
    public void onCreate(Bundle savedInstanceState) {//{{{
        super.onCreate(savedInstanceState);

        setContentView(R.layout.main);
        initView();

        mIot = IOTCloud.getInstance();
        new Thread(new Runnable() {
            @Override
            public void run() {
                Log.i(TAG,  " run iot ");
                int ret = 0;
                do {
                    ret = mIot.testService();
                    break;
                } while (ret != 0);
            }
        }).start();
    }//}}}

    private void initView() {//{{{
        mSignalBtn = (Button)findViewById(R.id.btn_signal);
        mBrightnessSB = (SeekBar)findViewById(R.id.brightness_sb);
        mVolUpBtn = (Button)findViewById(R.id.btn_volume_up);
        mVolDownBtn = (Button)findViewById(R.id.btn_volume_down);

        mSignalBtn.setOnClickListener(this);
        mVolUpBtn.setOnClickListener(this);
        mVolDownBtn.setOnClickListener(this);
        mBrightnessSB.setOnSeekBarChangeListener(this);
    }//}}}

    private class IOTReceiver extends BroadcastReceiver {//{{{
        @Override
        public void onReceive(Context context, Intent intent) {
            String action = intent.getAction();
            Log.i(TAG, "Action IOT: " + action);
        }
    }//}}}

    public void onProgressChanged(SeekBar seekBar, int progress, boolean fromUser) {//{{{
        mIot.updateDeviceShadow(Constants.IOT_PRO_BRIGHTNESS, String.valueOf(progress));
    }//}}}

    public void onStartTrackingTouch(SeekBar seekBar) {//{{{
    }//}}}

    public void onStopTrackingTouch(SeekBar seekBar) {//{{{
    }//}}}

    public void onClick(View v) {//{{{
        switch (v.getId()) {
            case R.id.btn_signal:
                startActivity(new Intent(MainActivity.this, SignalActivity.class));
                break;

            case R.id.btn_volume_up:
                mIot.contrlDeviceShadow(Constants.IOT_CMD_VOLUME_SWITCH, "\"shift\":\"up\"");
                break;

            case R.id.btn_volume_down:
                mIot.contrlDeviceShadow(Constants.IOT_CMD_VOLUME_SWITCH, "\"shift\":\"down\"");
                break;
        }
    }//}}}
}
