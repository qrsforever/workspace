package com.android.test.cashtoutiao;

import android.util.Log;
import android.support.test.uiautomator.UiAutomatorTestCase;
import android.support.test.uiautomator.UiDevice;
import android.support.test.uiautomator.UiObject;
import android.support.test.uiautomator.UiObjectNotFoundException;
import android.support.test.uiautomator.UiSelector;
import android.support.test.uiautomator.UiCollection;
import android.support.test.uiautomator.UiScrollable;

import org.junit.Test;

public class CashToutiaoAndroidTest extends UiAutomatorTestCase {

    public static final String TAG = CashToutiaoAndroidTest.class.getSimpleName();
    public UiDevice mDevice = null;
    public boolean mSignFlag = false;

    @Override
    protected void setUp() throws Exception {
        super.setUp();
        mDevice = getUiDevice();
    }

    @Test
    public void testDemo() throws UiObjectNotFoundException {
        int i = 0, sign = 0;
        for (i = 0; i < 9999; ++i) {
            try {
                Log.d(TAG, "Start CashToutiao");
                doStartApp();
            } catch (UiObjectNotFoundException e) {
            }

            try {
                Log.d(TAG, "Close AD");
                doCloseAD();
            } catch (UiObjectNotFoundException e) {
            }

            try {
                Log.d(TAG, "Hit Recieve");
                doRecieve50();
            } catch (UiObjectNotFoundException e) {
            }

            try {
                if (!mSignFlag) {
                    Log.d(TAG, "Do Tasks");
                    doTask();
                }
            } catch (UiObjectNotFoundException e) {
            }

            try {
                Log.d(TAG, "Do news");
                doNews();
            } catch (UiObjectNotFoundException e) {
            }

            try {
                Log.d(TAG, "Do Entertainment");
                doEntertainment(60);
            } catch (UiObjectNotFoundException e) {
            }
        }
    }

    public void doClearApps() throws UiObjectNotFoundException {
        try {
            // android4.4 or below, perhaps no permission
            Runtime.getRuntime().exec("am force-stop com.cashtoutiao");
            // android5.0 or above
            // mDevice.executeShellCommand("am force-stop com.cashtoutiao");
            Log.d(TAG, "Press Pecent apps");
            mDevice.pressRecentApps();
            sleep(1000);
        } catch (Exception e) {
        }
        UiScrollable allApps = new UiScrollable(new UiSelector().resourceId("com.android.systemui:id/recents_container"));
        UiObject app = allApps.getChild(new UiSelector().description("惠头条"));
        if (app.exists()) {
            app.swipeLeft(10); 
            sleep(500);
            // app.longClick();
            UiObject rmapp = new UiObject(new UiSelector().text("Remove from list"));
            if (rmapp.exists())
                rmapp.click();
        }
        // int count = allApps.getChildCount(new UiSelector().className ("android.widget.FrameLayout"));
        // Log.d(TAG, "Recent Apps count " + count);
        // for (int i = 0; i < count; ++i) {
        //     UiObject app = allApps.getChild(new UiSelector().className("android.widget.FrameLayout").instance(i));
        //     int r = mDevice.getDisplayRotation();
        //     int h = mDevice.getDisplayHeight();  //获取屏幕高度
        //     int w = mDevice.getDisplayWidth();   //获取屏幕宽度
        //     Log.d(TAG, "class = " + app.getClass());
        //     if (r == 3 || r == 1)
        //        app.swipeLeft(w);
        //     else
        //        app.swipeUp(h);
        //     sleep(1000);
        // }
    }

    public void doStartApp() throws UiObjectNotFoundException {
        mDevice.pressBack();
        mDevice.pressBack();
        mDevice.pressBack();
        doClearApps();
        mDevice.pressHome();
        // UiObject allAppsButton = new UiObject(new UiSelector().description("Apps"));
        // allAppsButton.clickAndWaitForNewWindow();
        // 如果惠头条在Home桌面
        UiObject toutiao = new UiObject(new UiSelector().text("惠头条"));
        toutiao.click();
        sleep(4000);
    }

    public void doCloseAD() throws UiObjectNotFoundException {
        UiObject closeAD = new UiObject(new UiSelector().resourceId("com.cashtoutiao:id/img_close"));
        closeAD.click();
        sleep(200);
    }

    public void doRecieve50() throws UiObjectNotFoundException {
        /* 领取50金币 */
        UiObject receive50 = new UiObject(new UiSelector().resourceId("com.cashtoutiao:id/yes_receive_layout"));
        receive50.click();
        sleep(200);
    }

    public void doNews() throws UiObjectNotFoundException {
        /* 头条 */
        UiCollection bottomTabs = new UiCollection(new UiSelector().resourceId("com.cashtoutiao:id/tabs"));
        UiObject news = bottomTabs.getChildByText(new UiSelector().className("android.widget.TextView"), "头条");
        news.click();
        sleep(200);
        /* UiScrollable items = new UiScrollable(new UiSelector().resourceId("android:id/list"));
         * UiObject first = items.getChild(new UiSelector().index(0));
         * first.click(); */
    }

    public void doEntertainment(int loop) throws UiObjectNotFoundException {
        /* 娱乐 */
        UiCollection newsTabs = new UiCollection(new UiSelector().resourceId("com.cashtoutiao:id/tab_news"));
        UiObject entertainment = newsTabs.getChildByText(new UiSelector().className("android.widget.TextView"), "娱乐");
        entertainment.click();
        sleep(1000);

        while (loop-- > 0) {
            UiScrollable items = new UiScrollable(new UiSelector().resourceId("android:id/list"));
            items.flingBackward();
            UiObject first = items.getChild(new UiSelector().index(0));
            first.click();
            sleep(1000);

            UiScrollable webpage = new UiScrollable(new UiSelector().resourceId("com.cashtoutiao:id/web_layout"));
            for (int i = 0; i < 20; ++i) {
                webpage.flingForward();
                sleep(3000);
                webpage.flingForward();
                sleep(3000);
                webpage.flingBackward();
                sleep(3000);
                webpage.flingBackward();
                sleep(3000);
            }
            UiObject back = new UiObject(new UiSelector().resourceId("com.cashtoutiao:id/iv_back"));
            back.click();
            sleep(1000);
        }
    }

    public void doTask() throws UiObjectNotFoundException {
        /* 底部的任务 */
        UiCollection bottomTabs = new UiCollection(new UiSelector().resourceId("com.cashtoutiao:id/tabs"));
        UiObject task = bottomTabs.getChildByText(new UiSelector().className("android.widget.TextView"), "任务中心");
        task.click();
        sleep(1000);

        /* Sign */
        UiObject sign = new UiObject(new UiSelector().resourceId("com.cashtoutiao:id/sign_btn_container"));
        sign.click();
        mSignFlag = true;
        sleep(1000);

        // UiScrollable taskItems = new UiScrollable(new UiSelector().resourceId("com.cashtoutiao:id/task_scroll"));
        // UiObject videoTask = new UiObject(new UiSelector().textMatches("^视频金币.*"));
        // taskItems.scrollIntoView(videoTask);
        // videoTask.click();
        // sleep(1000);

        // /* Video */
        // UiObject watchTask = new UiObject(new UiSelector().text("立即观看"));
        // watchTask.click();
        // sleep(1000);
        // try {
        //     doVideo(4);
        // } catch (UiObjectNotFoundException e) {
        // }
    }

    public void doVideo(int loop) throws UiObjectNotFoundException {
        while (loop-- > 0) {
            UiScrollable items = new UiScrollable(new UiSelector().resourceId("com.cashtoutiao:id/listview"));
            items.scrollForward();
            UiObject first = items.getChild(new UiSelector().index(0));
            first.click();
            sleep(30000);
            mDevice.pressBack();
        }
    }
}
