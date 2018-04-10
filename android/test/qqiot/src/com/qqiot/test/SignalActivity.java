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
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.RadioGroup.OnCheckedChangeListener;
import android.widget.SeekBar;
import android.widget.SeekBar.OnSeekBarChangeListener;
import android.view.View;
import android.view.View.OnClickListener;

public class SignalActivity extends Activity implements OnCheckedChangeListener {

    public static final String TAG = SignalActivity.class.getSimpleName();

    private static RadioGroup mSignalSelectRG = null;
    private static RadioButton mSignalMM = null;
    private static RadioButton mSignalHDMI1 = null;
    private static RadioButton mSignalHDMI2 = null;
    private static RadioButton mSignalHDMI3 = null;
    private static RadioButton mSignalDigital = null;
    private static RadioButton mSignalAnalog = null;
    private static RadioButton mSignalAV = null;

    @Override
    public void onCreate(Bundle savedInstanceState) {//{{{
        super.onCreate(savedInstanceState);

        setContentView(R.layout.signal);
        initView();

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

        mSignalSelectRG.setOnCheckedChangeListener(this);

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
        IOTCloud.getInstance().updateDeviceShadow(Constants.IOT_PRO_SIGNAL, val);
    }//}}}

}
