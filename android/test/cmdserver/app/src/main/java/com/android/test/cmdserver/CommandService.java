package com.android.test.cmdserver;

import android.app.Service;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.os.IBinder;
import android.os.Bundle;
import android.util.Log;

import android.app.AlarmManager;
import android.app.PendingIntent;
import java.io.DataOutputStream;
import java.io.IOException;

public class CommandService extends Service {
	protected String TAG = "QRS-CommandService";
	public boolean mQuitFlag = false;
	MyThread mThread = null;
	CommandReceiver mCmdReceiver;
    String mArgs;

    int mPid = -1;
    static int mScriptPid = -1;

	@Override
	public IBinder onBind(Intent intent) {
		Log.i(TAG, "onBind()");
		return null;
	}

	@Override
	public boolean onUnbind(Intent intent) {
		Log.i(TAG, "onUnbind()");
		return false;
	}

	@Override
	public void onCreate() {
		Log.i(TAG, "onCreate()");
		super.onCreate();
	}

	/* Called when Activity startService */
	@Override
	public int onStartCommand(Intent intent, int flags, int startId) {
		super.onStartCommand(intent, flags, startId);
		Log.i(TAG, "onStartCommand");

        mPid = android.os.Process.myPid();
		mCmdReceiver = new CommandReceiver();
		IntentFilter filter = new IntentFilter();
		filter.addAction("android.intent.action.cmdservice");
		registerReceiver(mCmdReceiver, filter);

        Bundle bundle = intent.getExtras();
        myStartService(bundle.getString("args", ""));
        return START_STICKY;
	}

	@Override
	public void onDestroy() {
		Log.i(TAG, "onDestroy()");
		super.onDestroy();
		this.unregisterReceiver(mCmdReceiver);
        // if (mThread != null)
        //     myStopService();
        // Intent intent = new Intent(this, MainActivity.class);
        // intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
        // PendingIntent restartIntent = PendingIntent.getActivity(context, 0, intent, 0);
        // AlarmManager mAlarmManager = (AlarmManager) context.getSystemService(Context.ALARM_SERVICE);
        // mAlarmManager.set(AlarmManager.RTC, System.currentTimeMillis() + 5000, restartIntent);
	}

    // Process[pid=2869]
    public int getPIDFromProcessToString(String s) {
        StringBuilder stringBuilder = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) >= '0' && s.charAt(i) <= '9') {
                stringBuilder.append(s.charAt(i));
            }
        }
        return Integer.valueOf(stringBuilder.toString());
    }

    public void sudo(String cmd, int flg) {
        try{
            Process su = Runtime.getRuntime().exec("su");
            if (1 == flg) {
                mScriptPid = getPIDFromProcessToString(su.toString());
                Log.d(TAG, "sudo program pid: " + mScriptPid);
            }
            DataOutputStream outputStream = new DataOutputStream(su.getOutputStream());
            outputStream.writeBytes(cmd + "\n");
            outputStream.flush();
            outputStream.writeBytes("exit\n");
            outputStream.flush();
            su.waitFor();
        }catch(IOException e){
             e.printStackTrace();
        }catch(InterruptedException e){
             e.printStackTrace();
        }
    }

	/*
	 * Thread runtime
	 */
	public class MyThread extends Thread {
		@Override
		public void run() {
			super.run();
            Log.d(TAG, "Thread run...");
            // int i = 5;
            // try {
                // while (i-- > 0) {
                    // showInfo("start lua: " + i);
                    // Thread.sleep(1000);
                // }
            // } catch (Exception e) {

            // }
            Intent intent = new Intent();
            intent.putExtra("cmd", Constants.CMD_LUALU_RUNNING);
            intent.setAction("android.intent.action.cmdactivity");
            sendBroadcast(intent);
			while(!mQuitFlag) {
				try {
                    Log.i(TAG, "BEG: /system/bin/sh /data/auto_lualu.sh " + mArgs);
                    sudo("/system/bin/sh /data/auto_lualu.sh " + mArgs, 1);
                    Log.i(TAG, "END: /system/bin/sh /data/auto_lualu.sh " + mArgs);
                    if (mQuitFlag)
                        break;
					Thread.sleep(10000);
                    Log.d(TAG, "quit, again");
				} catch(Exception e){
                    Log.d(TAG, "error");
					e.printStackTrace();
				}
			}
            Log.d(TAG, "MyThread Quit");
            intent = new Intent();
            intent.putExtra("cmd", Constants.CMD_LUALU_QUIT);
            intent.setAction("android.intent.action.cmdactivity");
            sendBroadcast(intent);
            mThread = null;
            mQuitFlag = false;
		}
	}

	/*
	 * Tell Activity to show message on screen
	 */
	public void showToast(String str) {
    	Intent intent = new Intent();
		intent.putExtra("cmd", Constants.CMD_SHOW_TOAST);
		intent.putExtra("str", str);
		intent.setAction("android.intent.action.cmdactivity");
		sendBroadcast(intent);
    }

	public void showInfo(String str) {
    	Intent intent = new Intent();
		intent.putExtra("cmd", Constants.CMD_SHOW_INFO);
		intent.putExtra("str", str);
		intent.setAction("android.intent.action.cmdactivity");
		sendBroadcast(intent);
    }

	/*
	 * Called by onStartCommand, initialize and start runtime thread
	 */
	private void myStartService(String args) {
        mArgs = args;
		//TODO initialize device
        Log.d(TAG, "myStartService");
        mQuitFlag = false;
        if (mThread == null) {
            mThread = new MyThread();
            mThread.start();
        }
	}

	/*
	 * Service stop after thread close
	 */
	public void myStopService() {
        Log.d(TAG, "myStopService");
		mQuitFlag = true;
        // new Thread(new Runnable() {
            // @Override
            // public void run() {
				try {
                    Log.i(TAG, "/system/bin/sh /data/auto_lualu.sh kill");
                    sudo("/system/bin/sh /data/auto_lualu.sh kill", 0);
					Thread.sleep(2000);
				} catch(Exception e){
                    Log.d(TAG, "error");
					e.printStackTrace();
				}
            // }
        // }).start();
        // try { 
        //     Log.i(TAG, "LUALU JOIN");
        //     mThread.join();
        //     Log.i(TAG, "LUALU END");
        // } catch (Exception e) {
        //     e.printStackTrace();
		// }
        // mThread = null;
        Log.d(TAG, "myStopService, scriptpid: " + mScriptPid);
        android.os.Process.killProcess(mScriptPid);
		stopSelf();
	}

	/*
	 * BroadcastReceiver for Activity
	 */
	private class CommandReceiver extends BroadcastReceiver{
		@Override
		public void onReceive(Context context, Intent intent) {
			if (intent.getAction().equals("android.intent.action.cmdservice")) {
				int cmd = intent.getIntExtra("cmd", -1);
                Log.d(TAG, "get cmd: " + cmd);
				int value = intent.getIntExtra("value", -1);
                switch (cmd) {
                    case Constants.CMD_STOP_SERVICE:
                        myStopService();
                        break;
                    case Constants.CMD_SEND_DATA:
                        myHandlerData(value);
                        break;
                    default:
                        ;
                }
			}
		}
	}

	public void myHandlerData(int value) {
		//TODO handle
		Log.i(TAG, "Recv " + value + " from broadcast.");
	}
}
