package com.hybroad.client;

import android.app.Activity;
import android.content.ComponentName;
import android.content.Intent;
import android.content.ServiceConnection;
import android.os.Bundle;
import android.os.IBinder;
import android.os.RemoteException;
import android.util.Log;

import com.hybroad.aidl.*;

public class AidlClientActivity extends Activity {
    public static final String TAG = "AidlClientActivity";
    public static final String BIND_ACTION = "com.hybroad.server.AidlServer";
    private IDemoServer mCalculate;
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);

        Intent it = new Intent();
        it.setAction(BIND_ACTION);
        startService(it);
        bindService(it, mServiceConnection, BIND_AUTO_CREATE);
    }

    ServiceConnection mServiceConnection = new ServiceConnection() {
        @Override
        public void onServiceConnected(ComponentName name, IBinder service) {
            Log.d(TAG, "onServiceConnected");
            mCalculate = IDemoServer.Stub.asInterface(service);
            OperandData o = new OperandData(6, "-", 1);
            if (mCalculate != null) {
                try {
                    mCalculate.calculate(o, mCallback);
                } catch (RemoteException e) {
                    e.printStackTrace();
                }
            }
        }

        @Override
        public void onServiceDisconnected(ComponentName name) {
            Log.d(TAG, "onServiceDisconnected");
        }
    };

    ICallback.Stub mCallback = new ICallback.Stub() {
        @Override
        public void displayResult(String result) throws RemoteException {
            Log.d(TAG, result);
        }
    };
}
