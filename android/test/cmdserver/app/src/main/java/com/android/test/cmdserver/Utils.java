package com.android.test.cmdserver;

import android.app.ActivityManager;
import android.content.Context;
import android.util.Log;
import android.text.TextUtils;

import java.util.ArrayList;
import java.lang.reflect.Method;

public class Utils {

    static final String TAG = "QRS-Utils";

    public static String getProperty(String key) {    
        try {    
            Class<?> c = Class.forName("android.os.SystemProperties");  
            Method get = c.getMethod("get", String.class, String.class);
            String value = (String)(get.invoke(c, key, "stop"));
            Log.d(TAG, "value = " + value);
            return value;
        } catch (Exception e) {
            Log.d(TAG, "getProperty====exception=");
            e.printStackTrace();
        }  
        return null;
    }

    public static void setProperty(String key, String value) {    
        try {    
            Class<?> c = Class.forName("android.os.SystemProperties");  
            Method set = c.getMethod("set", String.class, String.class);
            set.invoke(c, key, value );
        } catch (Exception e) {
            Log.d(TAG, "setProperty====exception=");
            e.printStackTrace();
        }  
    }

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
}
