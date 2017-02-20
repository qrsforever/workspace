package com.hybroad.server;

import android.app.Service;
import android.content.Intent;
import android.os.IBinder;
import android.os.RemoteException;
import android.util.Log;

import com.hybroad.aidl.*;

public class AidlServer extends Service {
    public static final String TAG = "AidlServer";
    @Override
    public IBinder onBind(Intent intent) {
        return mBinder;
    }

    IDemoServer.Stub mBinder = new IDemoServer.Stub() {
        @Override
        public int calculate(OperandData o, ICallback cb) throws RemoteException {
            Log.d(TAG, "calculate method is called");
            int d1 = o.data1;
            int d2 = o.data2;
            int result = 0;
            String oper = o.operator;
            if (oper.equals("+"))
                result = d1 + d2;
            else if (oper.equals("-"))
                result = d1 - d2;
            cb.displayResult("Calculate: " + d1 + " " + oper + " " + d2 + " = " + result);
            return result;
        }
    };
}
