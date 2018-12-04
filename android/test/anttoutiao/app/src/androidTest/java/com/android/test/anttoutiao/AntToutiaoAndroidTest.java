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
import android.support.test.uiautomator.Direction;
import android.support.test.uiautomator.By;
import android.support.test.uiautomator.UiObject2;
import android.support.test.uiautomator.Until;
import android.test.InstrumentationTestCase;

import org.junit.Test;
import java.util.List;

public class AntToutiaoAndroidTest extends InstrumentationTestCase {

    public static final String TAG = AntToutiaoAndroidTest.class.getSimpleName() + " qrs";
    public UiDevice mDevice = null;
    public static int mHeight = 1920;
    public static int mWidth = 1280;

    public static int mLoopCount = 4;
    public static int mNewsCount = 14;

    public static String[] mNewsLists = {
        "推荐", "热点", "搞笑", "健康", "推荐", "热点"
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
        mDevice = UiDevice.getInstance(getInstrumentation());
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
                    Thread.sleep(5000);
                    doTask();
                    flag = 1;
                }
            } catch (Exception e) {
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
            Thread.sleep(1000);
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
            Thread.sleep(6000);
        } catch (Exception e) {
            Log.d(TAG, "qrs start lite activity error: " + e);
        }
    }

    public void doEntertainment(int loop) throws UiObjectNotFoundException {
        try {
            UiObject2 bottomListView = mDevice.findObject(By.res("com.cashnews.spicy:id/tab_bottom_indicator"));
            List<UiObject2> childList = bottomListView.getChildren();
            if (childList.size() > 0) {
                UiObject2 task = childList.get(0);
                task.click();
            }
            Thread.sleep(200);
        } catch (Exception e) {
            Log.d(TAG, "qrs error: " + e);
            return;
        }
        for (int i = 0; i < loop; i++) {
            Log.d(TAG, "qrs loop: " + i + " vs " + loop);
            try {
                mDevice.executeShellCommand("am start -n  com.cashnews.spicy/com.cashnews.spicy.splash.activity.MainActivity");
                Thread.sleep(2000);
                try {
                    /* 有可能弹出了广告 */
                    int idx = new Random().nextInt(mNewsLists.length);
                    Log.d(TAG, "qrs news select : " + idx + " name:" + mNewsLists[idx]);
                    UiObject2 news = mDevice.findObject(By.text(mNewsLists[idx]));
                    if (news != null)
                        news.click();
                    Thread.sleep(3000);
                } catch (Exception e) {
                    Log.d(TAG, "qrs error: " + e);
                    mDevice.pressBack();
                }

                UiObject2 news_list = mDevice.findObject(By.res("com.cashnews.spicy:id/recycle_news_list"));
                int idx = new Random().nextInt(4);
                if (idx == 1) idx = 3;
                List<UiObject2> items = news_list.getChildren(); 
                if (items.size() == 0)
                    continue;
                if (idx >= items.size())
                    idx = 0;
                UiObject2 first = items.get(idx);
                first.click();
                Thread.sleep(1000);

                Log.d(TAG, "enter swipe");
                for (int j = 0; j < 24; ++j) {
                    Thread.sleep(new Random().nextInt(2000) + 500);
                    if (j < 12)
                        _Input_Swipe(360, 1280, 360, 600, 800);
                    else
                        _Input_Swipe(360, 600, 360, 1280, 800);
                }
                Log.d(TAG, "qrs try close this ad.");
                _Input_Tap(1180, 79);
                Thread.sleep(500);
                mDevice.pressBack();
            } catch (Exception e) {
                Log.d(TAG, "qrs error: " + e);
                mDevice.pressBack();
            }
            mDevice.pressBack();
        }
    }

    public void doTask() throws UiObjectNotFoundException {
        /* 底部的任务 */
        try {
            UiObject bottomListView = new UiObject(new UiSelector().resourceId("com.cashnews.spicy:id/tab_bottom_indicator"));
            UiObject task = bottomListView.getChild(new UiSelector().index(2));
            task.click();
            Thread.sleep(1000);
            Log.d(TAG, "------------> sign");
            UiObject sign = new UiObject(new UiSelector().resourceId("com.cashnews.spicy:id/iv_task_sign_in"));
            sign.click();
            Thread.sleep(200);
        } catch (Exception e) {
            Log.d(TAG, "qrs error: " + e);
            mDevice.pressBack();
        }

        /* 整点金币 */
        try {
            UiObject bottomListView = new UiObject(new UiSelector().resourceId("com.cashnews.spicy:id/tab_bottom_indicator"));
            UiObject task = bottomListView.getChild(new UiSelector().index(0));
            task.click();
            Thread.sleep(1000);
            Log.d(TAG, "qrs ------------> clock");
            UiObject clock = new UiObject(new UiSelector().resourceId("com.cashnews.spicy:id/img_clock_news"));
            clock.click();
            Thread.sleep(200);

            Log.d(TAG, "qrs ------------> sign-once");
            UiObject pan = new UiObject(new UiSelector().resourceId("com.cashnews.spicy:id/img_sign_in_news"));
            pan.click();
            Thread.sleep(200);

            _Input_Tap(620, 970);

            UiObject lottery = new UiObject(new UiSelector().resourceId("com.cashnews.spicy:id/img_close_lottery_web"));
            lottery.click();
            Thread.sleep(200);
            mDevice.pressBack();
        } catch (Exception e) {
            Log.d(TAG, "qrs error: " + e);
            mDevice.pressBack();
        }
    }

}
