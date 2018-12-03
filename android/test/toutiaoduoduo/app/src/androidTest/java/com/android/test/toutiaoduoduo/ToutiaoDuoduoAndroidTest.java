package com.android.test.toutiaoduoduo;

import android.util.Log;
import android.support.test.uiautomator.UiAutomatorTestCase;
import android.support.test.uiautomator.UiDevice;
import android.support.test.uiautomator.UiObject;
import android.support.test.uiautomator.UiObjectNotFoundException;
import android.support.test.uiautomator.UiSelector;
import android.support.test.uiautomator.UiCollection;
import android.support.test.uiautomator.UiScrollable;

import org.junit.Test;

public class ToutiaoDuoduoAndroidTest extends UiAutomatorTestCase {

    public static final String TAG = ToutiaoDuoduoAndroidTest.class.getSimpleName();
    public UiDevice mDevice = null;
    public static int mLoopCount = 24;
    public static int mNewsCount = 14;
    public static final int mPhoneType = 2;

    @Override
    protected void setUp() throws Exception {
        super.setUp();
        mDevice = getUiDevice();
    }

    @Test
    public void testDemo() throws UiObjectNotFoundException {
        int i, flag = 0;
        for (i = 0; i < mLoopCount; ++i) {
            try {
                Log.d(TAG, "qrs Start Toutiaoduoduo + i = " + i);
                doStartApp();
            } catch (UiObjectNotFoundException e) {
                Log.d(TAG, "qrs : " + e);
            }
            try {
                Log.d(TAG, "Do Tasks");
                if (flag == 0) {
                    doTask();
                    flag = 1;
                }
            } catch (UiObjectNotFoundException e) {
                Log.d(TAG, "qrs : " + e);
            }
            try {
                Log.d(TAG, "Do Entertainment mNewsCount: " + mNewsCount);
                doEntertainment(mNewsCount);
            } catch (UiObjectNotFoundException e) {
                Log.d(TAG, "qrs error: " + e);
            }
        }
    }

    public void doClearApps() throws UiObjectNotFoundException {
        try {
            mDevice.executeShellCommand("am force-stop com.lite.infoflow");
            Log.d(TAG, "Press Pecent apps");
            mDevice.pressRecentApps();
            sleep(1000);
        } catch (Exception e) {
        }
    }

    public void doStartApp() throws UiObjectNotFoundException {
        mDevice.pressBack();
        mDevice.pressBack();
        mDevice.pressBack();
        doClearApps();
        mDevice.pressHome();
        try {
            mDevice.executeShellCommand("am start -n  com.lite.infoflow/com.lite.infoflow.launcher.LauncherActivity");
            sleep(3000);
        } catch (Exception e) {
            Log.d(TAG, "qrs start lite activity error: " + e);
        }
    }

    public void doEntertainment(int loop) throws UiObjectNotFoundException {
        while (loop-- > 0) {
            try {
                Log.d(TAG, "qrs doEntertainment: loop = " + loop);
                /* 娱乐 */
                UiObject task = new UiObject(new UiSelector().text("首页"));
                task.click();
                sleep(1000);

                UiObject et = new UiObject(new UiSelector().text("娱乐"));
                et.click();
                sleep(1000);
                // try {
                //     UiScrollable items = new UiScrollable(new UiSelector().className("android.support.v4.view.ViewPager"));
                //     items.flingBackward();
                //     UiObject first = items.getChild(new UiSelector().index(0));
                //     first.click();
                //     sleep(200);
                // } catch (UiObjectNotFoundException e) {
                //     sleep(200);
                // }
                mDevice.executeShellCommand("input swipe 350 350 350 750 800");
                sleep(1000);
                mDevice.executeShellCommand("input tap 350 350");
                sleep(3000);
                for (int i = 0; i < 6; ++i) {
                    mDevice.executeShellCommand("input swipe 350 950 350 250 1000");
                    sleep(2000);
                }
                mDevice.pressBack();
            } catch (Exception e) {
                Log.d(TAG, "qrs error: " + e);
            }
        }
        mDevice.pressBack();
    }

    public void doTask() throws UiObjectNotFoundException {
        /* 底部的任务 */
        UiObject task = new UiObject(new UiSelector().text("赚钱"));
        task.click();
        sleep(1000);
    }
}
