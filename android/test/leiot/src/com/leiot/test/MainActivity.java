package com.leiot.test;

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
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.RadioGroup.OnCheckedChangeListener;
import android.widget.SeekBar;
import android.widget.SeekBar.OnSeekBarChangeListener;

public class MainActivity extends Activity implements
       OnCheckedChangeListener, OnSeekBarChangeListener {
    public static final String TAG = MainActivity.class.getSimpleName();
    TVDeviceShadow mIot;
    IOTReceiver mIotReceiver = null;

    private static RadioGroup mSignalSelectRG = null;
    private static RadioButton mSignalMM = null;
    private static RadioButton mSignalHDMI1 = null;
    private static RadioButton mSignalHDMI2 = null;
    private static RadioButton mSignalHDMI3 = null;
    private static RadioButton mSignalDigital = null;
    private static RadioButton mSignalAnalog = null;
    private static RadioButton mSignalAV = null;
    private static TextView mVolumeSwitch = null;

    private static SeekBar mBrightnessSB = null;

    @Override
    public void onCreate(Bundle savedInstanceState) {//{{{
        super.onCreate(savedInstanceState);

        setContentView(R.layout.main);
        initView();

        mIotReceiver = new IOTReceiver();
        IntentFilter filter = new IntentFilter();
        filter.addAction(Constants.IOT_ACTION_PRO_SIGNAL);
        filter.addAction(Constants.IOT_ACTION_PRO_BRIGHTNESS);
        filter.addAction(Constants.IOT_CMD_VOLUME_SWITCH);
        filter.addAction(Constants.IOT_CMD_CHANNEL_SWITCH);
        filter.addAction(Constants.IOT_CMD_APP_START);
        filter.addAction(Constants.IOT_CMD_VIDEO_SEARCH);
        filter.addAction(Constants.IOT_CMD_TEXT_PUSH);
        filter.addAction(Constants.IOT_CMD_VIDEO_PLAY);
        registerReceiver(mIotReceiver, filter);

        mIot = TVDeviceShadow.getInstance(this);
        new Thread(new Runnable() {
            @Override
            public void run() {
                int ret = 0;
                do {
                    ret = mIot.iotConnService(60000);
                    Log.i(TAG, "iotConnService ret = " + ret);
                } while (ret != 0);
            }
        }).start();
    }//}}}

    private void initView() {//{{{
        mSignalSelectRG = (RadioGroup)findViewById(R.id.input_sex_rg);
        mSignalMM = (RadioButton)findViewById(R.id.input_mm);
        mSignalHDMI1 = (RadioButton)findViewById(R.id.input_hdmi1);
        mSignalHDMI2 = (RadioButton)findViewById(R.id.input_hdmi2);
        mSignalHDMI3 = (RadioButton)findViewById(R.id.input_hdmi3);
        mSignalDigital = (RadioButton)findViewById(R.id.input_digital);
        mSignalAnalog = (RadioButton)findViewById(R.id.input_analog);
        mSignalAV = (RadioButton)findViewById(R.id.input_av);
        mBrightnessSB = (SeekBar)findViewById(R.id.brightness_sb);
        mVolumeSwitch = (TextView)findViewById(R.id.volume_switch_tv);

        mSignalSelectRG.setOnCheckedChangeListener(this);
        mBrightnessSB.setOnSeekBarChangeListener(this);
    }//}}}

    private class IOTReceiver extends BroadcastReceiver {//{{{
        @Override
        public void onReceive(Context context, Intent intent) {
            String action = intent.getAction();
            Log.i(TAG, "Action IOT: " + action);
            String val = (String)intent.getStringExtra("value");
            if (action.equals(Constants.IOT_ACTION_PRO_SIGNAL)) {
                if (val.equals("0")) {
                    mSignalSelectRG.check(R.id.input_mm);
                } else if (val.equals("1")) {
                    mSignalSelectRG.check(R.id.input_hdmi1);
                } else if (val.equals("2")) {
                    mSignalSelectRG.check(R.id.input_hdmi2);
                } else if (val.equals("3")) {
                    mSignalSelectRG.check(R.id.input_hdmi3);
                } else if (val.equals("4")) {
                    mSignalSelectRG.check(R.id.input_digital);
                } else if (val.equals("5")) {
                    mSignalSelectRG.check(R.id.input_analog);
                } else if (val.equals("6")) {
                    mSignalSelectRG.check(R.id.input_av);
                }
            } else if (action.equals(Constants.IOT_ACTION_PRO_BRIGHTNESS)) {
                mBrightnessSB.setProgress(Integer.parseInt(val));
            } else if (action.equals(Constants.IOT_CMD_VOLUME_SWITCH)) {
                mVolumeSwitch.setText(val);
            }
        }
    }//}}}

    public void onCheckedChanged(RadioGroup rg, int checkedId) {//{{{
        String val = "0";
        switch (checkedId) {
            case R.id.input_mm:
                val = "0";
                break;
            case R.id.input_hdmi1:
                val = "1";
                break;
            case R.id.input_hdmi2:
                val = "2";
                break;
            case R.id.input_hdmi3:
                val = "3";
                break;
            case R.id.input_digital:
                val = "4";
                break;
            case R.id.input_analog:
                val = "5";
                break;
            case R.id.input_av:
                val = "6";
                break;
        }
        mIot.updatePropertyFromUI(Constants.IOT_PRO_SIGNAL, val, true);
    }//}}}

    public void onProgressChanged(SeekBar seekBar, int progress, boolean fromUser) {//{{{
        mIot.updatePropertyFromUI(Constants.IOT_PRO_BRIGHTNESS, String.valueOf(progress), false);
    }//}}}

    public void onStartTrackingTouch(SeekBar seekBar) {//{{{
    }//}}}

    public void onStopTrackingTouch(SeekBar seekBar) {//{{{
    }//}}}
}
