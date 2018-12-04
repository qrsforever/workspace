package com.android.test.toutiaoduoduo;

import android.util.Log;
import java.util.Random;
import android.support.test.uiautomator.UiAutomatorTestCase;
import android.support.test.uiautomator.UiDevice;
import android.support.test.uiautomator.UiObject;
import android.support.test.uiautomator.UiObjectNotFoundException;
import android.support.test.uiautomator.UiSelector;
import android.support.test.uiautomator.UiCollection;
import android.support.test.uiautomator.UiScrollable;

import org.junit.Test;

public class AntToutiaoAndroidTest extends UiAutomatorTestCase {

    public static final String TAG = AntToutiaoAndroidTest.class.getSimpleName() + " qrs";
    public UiDevice mDevice = null;
    public static int mHeight = 1920;
    public static int mWidth = 1280;

    public static int mLoopCount = 4;
    public static int mNewsCount = 14;

    public static String[] mNewsLists = {
        "推荐", "热点", "搞笑", "健康", "推荐"
    };

    private void _Input_Swipe(int x1, int y1, int x2, int y2, int tm) throws Exception {
        int x_1 = (int)((x1 * mWidth) / 1280);
        int y_1 = (int)((y1 * mHeight) / 1920);
        int x_2 = (int)((x2 * mWidth) / 1280);
        int y_2 = (int)((y2 * mHeight) / 1920);

        mDevice.executeShellCommand("input swipe " + x_1 + " " + y_1 + " " + x_2 + " " + y_2 + " " + tm);
    }

    private void _Input_Tap(int x1, int y1) throws Exception {
        int x_1 = (int)((x1 * mWidth) / 1280);
        int y_1 = (int)((y1 * mHeight) / 1920);

        mDevice.executeShellCommand("input tap " + x_1 + " " + y_1);
    }

    @Override
    protected void setUp() throws Exception {
        super.setUp();
        mDevice = getUiDevice();
        mHeight = mDevice.getDisplayHeight();  
        mWidth = mDevice.getDisplayWidth(); 
    }

    @Test
    public void testDemo() throws UiObjectNotFoundException {
        int i, flag = 0;
        for (i = 0; i < mLoopCount; ++i) {
            try {
                Log.d(TAG, "qrs Start AntToutiao + i = " + i);
                doStartApp();
            } catch (UiObjectNotFoundException e) {
                Log.d(TAG, "qrs : " + e);
            }
            try {
                Log.d(TAG, "qrs Do Tasks");
                if (flag == 0) {
                    sleep(5000);
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
            mDevice.executeShellCommand("am force-stop com.cashnews.spicy");
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
            mDevice.executeShellCommand("am start -n  com.cashnews.spicy/com.cashnews.spicy.splash.activity.SplashActivity");
            sleep(6000);
        } catch (Exception e) {
            Log.d(TAG, "qrs start lite activity error: " + e);
        }
    }

    public void doEntertainment(int loop) throws UiObjectNotFoundException {
        for (int i = 0; i < loop; loop--) {
            Log.d(TAG, "qrs loop = " + loop);
            try {
                try {
                    UiObject bottomListView = new UiObject(new UiSelector().resourceId("com.cashnews.spicy:id/tab_bottom_indicator"));
                    UiObject task = bottomListView.getChild(new UiSelector().index(0));
                    task.click();
                    sleep(200);
                } catch (Exception e) {
                    Log.d(TAG, "qrs error: " + e);
                    /* 有可能弹出了广告 */
                    sleep(12000);
                    _Input_Tap(1180, 60);
                    mDevice.pressBack();
                    loop++;
                    continue;
                }

                int idx = new Random().nextInt(mNewsLists.length);
                UiObject news = new UiObject(new UiSelector().text(mNewsLists[idx]));
                news.click();
                sleep(200);

                UiScrollable pager = new UiScrollable(new UiSelector().resourceId("com.cashnews.spicy:id/viewpager_news"));
                pager.flingBackward();

                sleep(1000);
                UiScrollable items = new UiScrollable(new UiSelector().resourceId("com.cashnews.spicy:id/recycle_news_list"));
                idx = new Random().nextInt(4);
                if (idx == 1) idx = 0;
                UiObject first = items.getChild(new UiSelector().index(idx));
                first.click();
                sleep(200);

                for (int j = 0; j < 6; ++j) {
                    _Input_Swipe(360, 1280, 360, 400, 800);
                    sleep(new Random().nextInt(2000) + 500);
                }
                mDevice.pressBack();
            } catch (Exception e) {
                Log.d(TAG, "qrs error: " + e);
                mDevice.pressBack();
            }
        }
    }

    public void doTask() throws UiObjectNotFoundException {
        /* 底部的任务 */
        try {
            UiObject bottomListView = new UiObject(new UiSelector().resourceId("com.cashnews.spicy:id/tab_bottom_indicator"));
            UiObject task = bottomListView.getChild(new UiSelector().index(2));
            task.click();
            sleep(1000);
            Log.d(TAG, "------------> sign");
            UiObject sign = new UiObject(new UiSelector().resourceId("com.cashnews.spicy:id/iv_task_sign_in"));
            sign.click();
            sleep(200);
        } catch (Exception e) {
            Log.d(TAG, "qrs error: " + e);
            mDevice.pressBack();
        }

        /* 整点金币 */
        try {
            UiObject bottomListView = new UiObject(new UiSelector().resourceId("com.cashnews.spicy:id/tab_bottom_indicator"));
            UiObject task = bottomListView.getChild(new UiSelector().index(0));
            task.click();
            sleep(1000);
            Log.d(TAG, "qrs ------------> clock");
            UiObject clock = new UiObject(new UiSelector().resourceId("com.cashnews.spicy:id/img_clock_news"));
            clock.click();
            sleep(200);

            Log.d(TAG, "qrs ------------> sign-once");
            UiObject pan = new UiObject(new UiSelector().resourceId("com.cashnews.spicy:id/img_sign_in_news"));
            pan.click();
            sleep(200);

            _Input_Tap(620, 970);

            UiObject lottery = new UiObject(new UiSelector().resourceId("com.cashnews.spicy:id/img_close_lottery_web"));
            lottery.click();
            sleep(200);
            mDevice.pressBack();
        } catch (Exception e) {
            Log.d(TAG, "qrs error: " + e);
            mDevice.pressBack();
        }
    }

}
