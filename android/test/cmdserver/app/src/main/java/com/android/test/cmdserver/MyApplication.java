package com.android.test.cmdserver;

import android.app.Application;
import android.app.Activity;
import java.util.List;
import java.util.ArrayList;
import android.util.Log;

public class MyApplication extends Application {
    List<Activity> list = new ArrayList<>();
    protected String TAG = "QRS-MyApplication";

    @Override
    public void onCreate() {
        super.onCreate();
        Log.d(TAG, "onCreate");
        MyUncaughtExceptionHandler catchException = new MyUncaughtExceptionHandler(getApplicationContext());
        Thread.setDefaultUncaughtExceptionHandler(catchException);
    }
    public void removeActivity(Activity a) {
        list.remove(a);
    }
    public void addActivity(Activity a) {
        list.add(a);
    }
    public void finishActivity() {
        for (Activity activity : list) {
            if (null != activity) {
                activity.finish();
            }
        }
        android.os.Process.killProcess(android.os.Process.myPid());
    }
}
