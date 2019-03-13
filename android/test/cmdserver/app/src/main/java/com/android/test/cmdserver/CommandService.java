package com.android.test.cmdserver;

import android.app.Service;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.os.IBinder;
import android.util.Log;

import java.io.DataOutputStream;
import java.io.IOException;

public class CommandService extends Service {
	protected String TAG = "CommandService";
	public boolean mQuitFlag = true;
	MyThread mThread;
	CommandReceiver mCmdReceiver;

	/* Define service command */
	static final int CMD_START_SERVICE = 0x00;
	static final int CMD_STOP_SERVICE = 0x01;
	static final int CMD_SYSTEM_EXIT  = 0x02;
	static final int CMD_SHOW_TOAST   = 0x03;
	static final int CMD_SEND_DATA    = 0x04;
    static final int CMD_SHOW_INFO    = 0x05;

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

		mCmdReceiver = new CommandReceiver();
		IntentFilter filter = new IntentFilter();
		filter.addAction("android.intent.action.cmdservice");
		registerReceiver(mCmdReceiver, filter);

		myStartService();
		return super.onStartCommand(intent, flags, startId);
	}

	@Override
	public void onDestroy() {
		Log.i(TAG, "onDestroy()");
		super.onDestroy();
		this.unregisterReceiver(mCmdReceiver);
		mQuitFlag = false;
		boolean retry = true;
		while (retry) {
			try {
				retry = false;
				mThread.join();
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
	}

    public void sudo(String cmd) {
        try{
            Process su = Runtime.getRuntime().exec("su");
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
            int i = 5;
            try {
                while (i-- > 0) {
                    showInfo("start lua: " + i);
                    Thread.sleep(1000);
                }
            } catch (Exception e) {

            }
			while(mQuitFlag) {
				try {
                    showToast("lua num:" + i);
                    Log.i(TAG, "/system/bin/sh /data/auto_lualu.sh");
                    sudo("/system/bin/sh /data/auto_lualu.sh");
                    ++i;
					Thread.sleep(10000);
				} catch(Exception e){
					e.printStackTrace();
				}
			}
		}
	}

	/*
	 * Tell Activity to show message on screen
	 */
	public void showToast(String str) {
    	Intent intent = new Intent();
		intent.putExtra("cmd", CMD_SHOW_TOAST);
		intent.putExtra("str", str);
		intent.setAction("android.intent.action.cmdactivity");
		sendBroadcast(intent);
    }

	public void showInfo(String str) {
    	Intent intent = new Intent();
		intent.putExtra("cmd", CMD_SHOW_INFO);
		intent.putExtra("str", str);
		intent.setAction("android.intent.action.cmdactivity");
		sendBroadcast(intent);
    }

	/*
	 * Called by onStartCommand, initialize and start runtime thread
	 */
	private void myStartService() {
		//TODO initialize device
		mQuitFlag = true;
		mThread = new MyThread();
		mThread.start();
	}

	/*
	 * Service stop after thread close
	 */
	public void myStopService() {
		mQuitFlag = false;
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
				int value = intent.getIntExtra("value", -1);
                switch (cmd) {
                    case CMD_STOP_SERVICE:
                        myStopService();
                    case CMD_SEND_DATA:
                        myHandlerData(value);
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
