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

    @Override
    protected void setUp() throws Exception {
        super.setUp();
        mDevice = getUiDevice();
    }

    @Test
    public void testDemo() throws UiObjectNotFoundException {
        int i, flag = 0;
        int count = 40;
        for (i = 0; i < count; ++i) {
            try {
                Log.d(TAG, "Start CashToutiao");
                doStartApp();
            } catch (UiObjectNotFoundException e) {
                Log.d(TAG, "qrs : " + e);
            }

            try {
                Log.d(TAG, "Close AD");
                doCloseAD();
            } catch (UiObjectNotFoundException e) {
                Log.d(TAG, "qrs : " + e);
            }

            // try {
            //     Log.d(TAG, "Login");
            //     if (flag == 0) {
            //         if (i < count / 2)
            //             doLogin("15801310416", "20150505");
            //         else
            //             doLogin("18811165327", "ting1412");
            //     }
            // } catch (UiObjectNotFoundException e) {
            //     Log.d(TAG, "qrs : " + e);
            // }

            try {
                Log.d(TAG, "Hit Recieve");
                doRecieve50();
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

            /*
            try {
                Log.d(TAG, "Do news");
                doNews();
            } catch (UiObjectNotFoundException e) {
                Log.d(TAG, "qrs : " + e);
            }
            */
            try {
                Log.d(TAG, "Do Entertainment");
                doEntertainment(20);
            } catch (UiObjectNotFoundException e) {
                Log.d(TAG, "qrs : " + e);
            }

            // try {
            //     Log.d(TAG, "Do Video");
            //     doVideo(12);
            // } catch (UiObjectNotFoundException e) {
            //     Log.d(TAG, "qrs : " + e);
            // }

            // if (i == count / 2) {
            //     try {
            //         Log.d(TAG, "Logout");
            //         doLogout();
            //     } catch (UiObjectNotFoundException e) {
            //         Log.d(TAG, "qrs : " + e);
            //     }
            //     flag = 0;
            // }
        }
    }

    public void doClearApps() throws UiObjectNotFoundException {
        try {
            // android4.4 or below, perhaps no permission
            // Runtime.getRuntime().exec("am force-stop com.cashtoutiao");
            // android5.0 or above
            mDevice.executeShellCommand("am force-stop com.cashtoutiao");
            Log.d(TAG, "Press Pecent apps");
            mDevice.pressRecentApps();
            sleep(1000);
        } catch (Exception e) {
        }
        UiScrollable allApps = new UiScrollable(new UiSelector().resourceId("com.android.systemui:id/recents_container"));
        UiObject app = allApps.getChild(new UiSelector().description("惠头条"));
        if (app.exists()) {
            app.swipeLeft(10);
            sleep(1000);
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
        try {
            UiObject not = new UiObject(new UiSelector().text("以后再说"));
            not.click();
        } catch (UiObjectNotFoundException e) {
            Log.d(TAG, "qrs : " + e);
        }
    }

    public void doLogin(String u, String c) throws UiObjectNotFoundException {
        /* 登录 */
        try {
            UiObject user = new UiObject(new UiSelector().resourceId("com.cashtoutiao:id/username"));
            user.setText(u);
            UiObject pass = new UiObject(new UiSelector().resourceId("com.cashtoutiao:id/password"));
            pass.setText(c);
            UiObject login = new UiObject(new UiSelector().resourceId("com.cashtoutiao:id/login_button"));
            login.click();
            sleep(200);
        } catch (UiObjectNotFoundException e) {
            Log.d(TAG, "qrs : " + e);
        }
    }

    public void doLogout() throws UiObjectNotFoundException {
        /* 我的 */
        UiCollection bottomTabs = new UiCollection(new UiSelector().resourceId("com.cashtoutiao:id/tabs"));
        UiObject me = bottomTabs.getChildByText(new UiSelector().className("android.widget.TextView"), "我的");
        me.click();
        sleep(200);

        /* 点击设置 */
        UiObject set = new UiObject(new UiSelector().text("设置"));
        set.click();
        sleep(200);

        /* 划到底部 */
        UiScrollable setitems = new UiScrollable(new UiSelector().resourceId("com.cashtoutiao:id/content_container"));
        setitems.flingForward();

        /* 登出 */
        UiObject logout = new UiObject(new UiSelector().resourceId("com.cashtoutiao:id/layout_logout"));
        logout.click();

        /* 确定退出*/
        UiObject quit = new UiObject(new UiSelector().text("退出登录"));
        quit.click();
        sleep(200);
    }

    public void doRecieve50() throws UiObjectNotFoundException {
        /* 领取50金币 */
        UiObject receive50 = new UiObject(new UiSelector().resourceId("com.cashtoutiao:id/yes_receive_layout"));
        receive50.click();
        sleep(200);

        try {
            UiObject ignore = new UiObject(new UiSelector().text("忽略"));
            ignore.click();
        } catch (UiObjectNotFoundException e) {
            Log.d(TAG, "qrs : " + e);
        }
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
            for (int i = 0; i < 6; ++i) {
                webpage.flingForward();
                sleep(2000);
                webpage.flingForward();
                sleep(2000);
                webpage.flingBackward();
                sleep(2000);
                webpage.flingBackward();
                sleep(2000);
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
        sleep(1000);

        // UiScrollable taskItems = new UiScrollable(new UiSelector().resourceId("com.cashtoutiao:id/task_scroll"));
        // UiObject videoTask = new UiObject(new UiSelector().textMatches("^视频金币.*"));
        // taskItems.scrollIntoView(videoTask);
        // videoTask.click();
        // sleep(1000);

        /* Video */
        // UiObject watchTask = new UiObject(new UiSelector().text("立即观看"));
        // watchTask.click();
        // sleep(1000);
        // try {
        //     doVideo(12);
        // } catch (UiObjectNotFoundException e) {
        // }
    }

    public void doVideo(int loop) throws UiObjectNotFoundException {
        /* 视频 */
        while (loop-- > 0) {
            UiCollection newsTabs = new UiCollection(new UiSelector().resourceId("com.cashtoutiao:id/tab_news"));
            UiObject video = newsTabs.getChildByText(new UiSelector().className("android.widget.TextView"), "视频");
            video.click();
            sleep(30000);
            mDevice.pressBack();
        }
        // while (loop-- > 0) {
        //     UiScrollable items = new UiScrollable(new UiSelector().resourceId("com.cashtoutiao:id/listview"));
        //     items.scrollForward();
        //     UiObject first = items.getChild(new UiSelector().index(0));
        //     first.click();
        //     sleep(30000);
        //     mDevice.pressBack();
        // }
    }
}
