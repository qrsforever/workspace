package com.hybroad.client;

import java.util.Random;

import android.app.Activity;
import android.os.Bundle;
import android.os.RemoteException;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.hybroad.aidl.IQAudioService;

public class AudioClientActivity extends Activity implements OnClickListener {
    IQAudioService mAudioService = null;
    Button btnSet;
    Button btnGet;
    TextView tvShow = null;
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        btnSet = (Button)this.findViewById(R.id.set_vol);
        btnGet = (Button)this.findViewById(R.id.get_vol);
        tvShow = (TextView)this.findViewById(R.id.show_value);
        btnSet.setOnClickListener(this);
        btnGet.setOnClickListener(this);
        mAudioService = QAudioManager.getService();
    }

    @Override
    public void onClick(View v) {
        switch (v.getId()) {
            case R.id.set_vol:
                try {
                    int value = (int)(Math.random()*100 + 1);
                    mAudioService.setVolume(value);
                    if (tvShow != null)
                        tvShow.setText("set value: " + value);
                } catch (RemoteException e) {
                    e.printStackTrace();
                }
                break;
            case R.id.get_vol:
                try {
                    int value = mAudioService.getVolume();
                    if (tvShow != null)
                        tvShow.setText("get value: " + value);
                } catch (RemoteException e) {
                    e.printStackTrace();
                }
                break;
            default:
                break;
        }

    }
}
