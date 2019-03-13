package com.android.test.cmdserver;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.app.AlarmManager;
import android.app.PendingIntent;
import android.os.Looper;
import android.widget.Toast;

public class MyUncaughtExceptionHandler implements Thread.UncaughtExceptionHandler {
    private Context context;
    private Thread.UncaughtExceptionHandler mUncaughtExceptionHandler;
    private MyApplication myApplication;

    public MyUncaughtExceptionHandler(Context context) {
        this.context = context;
        mUncaughtExceptionHandler = Thread.getDefaultUncaughtExceptionHandler();
        myApplication = new MyApplication();
    }

    @Override
    public void uncaughtException(Thread thread, Throwable ex) {
        if (!handleException(ex) && mUncaughtExceptionHandler != null) {
           mUncaughtExceptionHandler.uncaughtException(thread, ex);
        } else {
            Intent intent = new Intent(context, MainActivity.class);
            intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
            PendingIntent restartIntent = PendingIntent.getActivity(context, 0, intent, 0);
            AlarmManager mAlarmManager = (AlarmManager) context.getSystemService(Context.ALARM_SERVICE);
            mAlarmManager.set(AlarmManager.RTC, System.currentTimeMillis() + 5000, restartIntent);
            myApplication.finishActivity();
        }
    }

    private boolean handleException(Throwable ex) {
        if (ex == null) {
            return false;
        }
        new Thread() {
            @Override
            public void run() {
                Looper.prepare();
                Toast.makeText(context, "Sorry, program error, restarting...", Toast.LENGTH_SHORT).show();
                Looper.loop();
            }
        }.start();
        return true;
    }
}
