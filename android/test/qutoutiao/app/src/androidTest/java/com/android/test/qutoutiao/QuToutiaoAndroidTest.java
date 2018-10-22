package com.android.test.qutoutiao;

import android.util.Log;
import android.support.test.uiautomator.UiAutomatorTestCase;
import android.support.test.uiautomator.UiDevice;
import android.support.test.uiautomator.UiObject;
import android.support.test.uiautomator.UiObjectNotFoundException;
import android.support.test.uiautomator.UiSelector;
import android.support.test.uiautomator.UiCollection;
import android.support.test.uiautomator.UiScrollable;

import org.junit.Test;

public class QuToutiaoAndroidTest extends UiAutomatorTestCase {

    public static final String TAG = QuToutiaoAndroidTest.class.getSimpleName();
    public UiDevice mDevice = null;
    public static int mLoopCount = 24;
    public static int mNewsCount = 14;

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
                Log.d(TAG, "qrs Start QuToutiao + i = " + i);
                doStartApp();
            } catch (UiObjectNotFoundException e) {
                Log.d(TAG, "qrs : " + e);
            }

            try {
                if (flag == 0) {
                    if (i < mLoopCount / 2) {
                        Log.d(TAG, "qrs Login 188");
                        doLogin("18811165327", "20150505");
                    } else {
                        Log.d(TAG, "qrs Login 158");
                        doLogin("15801310416", "20150505");
                    }
                }
            } catch (UiObjectNotFoundException e) {
                Log.d(TAG, "qrs : " + e);
            }

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

            // try {
                // Log.d(TAG, "Do news");
                // doNews();
            // } catch (UiObjectNotFoundException e) {
            // }

            try {
                Log.d(TAG, "Do Entertainment mNewsCount: " + mNewsCount);
                doEntertainment(mNewsCount);
            } catch (UiObjectNotFoundException e) {
                Log.d(TAG, "qrs error: " + e);
            }

            // try {
            //     Log.d(TAG, "Do Video");
            //     doVideo(12);
            // } catch (UiObjectNotFoundException e) {
            // }

            if ( i == mLoopCount / 2) {
                try {
                    Log.d(TAG, "Logout");
                    doLogout();
                    flag = 0;
                } catch (UiObjectNotFoundException e) {
                    Log.d(TAG, "qrs : " + e);
                }
            }
        }
        try {
            Log.d(TAG, "qrs end Logout");
            doLogout();
            flag = 0;
        } catch (UiObjectNotFoundException e) {
            Log.d(TAG, "qrs : " + e);
        }
    }

    public void doClearApps() throws UiObjectNotFoundException {
        try {
            // android4.4 or below, perhaps no permission
            // Runtime.getRuntime().exec("am force-stop com.jifen.qukan");
            // android5.0 or above
            mDevice.executeShellCommand("am force-stop com.jifen.qukan");
            Log.d(TAG, "Press Pecent apps");
            mDevice.pressRecentApps();
            sleep(1000);
        } catch (Exception e) {
        }
        UiScrollable allApps = new UiScrollable(new UiSelector().resourceId("com.android.systemui:id/recents_container"));
        UiObject app = allApps.getChild(new UiSelector().description("趣头条"));
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
        UiObject toutiao = new UiObject(new UiSelector().text("趣头条"));
        toutiao.click();
        sleep(2000);

        try {
            UiObject notupdate = new UiObject(new UiSelector().text("以后更新"));
            notupdate.click();
            sleep(1000);
        } catch (Exception e) {
            Log.d(TAG, "qrs : " + e);
        }

        try {
            UiObject rej = new UiObject(new UiSelector().text("先去逛逛"));
            rej.click();
            sleep(1000);
        } catch (Exception e) {
            Log.d(TAG, "qrs : " + e);
        }
    }

    public int onClickMine() throws UiObjectNotFoundException {
        /* 点击我的 */
        try {
            UiObject me = new UiObject(new UiSelector().text("我的"));
            me.click();
        } catch (UiObjectNotFoundException e) {
            Log.d(TAG, "qrs : " + e);
        }

        /* 关闭领取红包 */
        try {
            UiObject closered = new UiObject(new UiSelector().resourceId("com.jifen.qukan:id/p2"));
            closered.click();
        } catch (Exception e) {
            Log.d(TAG, "qrs : " + e);
        }
        return 0;
    }

    public void doLogin(String u, String c) throws UiObjectNotFoundException {
        /* 点击我的,消除障碍 */
        onClickMine();
        try {
            UiObject kf = new UiObject(new UiSelector().text("联系客服"));
            kf.click();
            mDevice.pressBack();
        } catch (UiObjectNotFoundException e) {
            /* 已经登录, 转到头条栏 */
            try {
                UiObject toutiao = new UiObject(new UiSelector().resourceId("com.jifen.qukan:id/jx"));
                toutiao.click();
                sleep(1000);
            } catch (UiObjectNotFoundException e1) { 
                Log.d(TAG, "qrs : " + e1);
            }
            return;
        }

        UiObject cl = new UiObject(new UiSelector().text("密码登录"));
        cl.click();
        
        UiObject user = new UiObject(new UiSelector().resourceId("com.jifen.qukan:id/aaz"));
        user.setText(u);
        UiObject code = new UiObject(new UiSelector().resourceId("com.jifen.qukan:id/ab1"));
        code.setText(c);

        UiObject login = new UiObject(new UiSelector().resourceId("com.jifen.qukan:id/me"));
        login.click();
    }

    public void doLogout() throws UiObjectNotFoundException {
        mDevice.pressBack();

        /* 点击我的,消除障碍 */
        onClickMine();

        /* 点击设置 */
        UiScrollable meitems = new UiScrollable(new UiSelector().resourceId("com.jifen.qukan:id/ue"));
        meitems.flingForward();
        meitems.flingForward();
        UiObject set = new UiObject(new UiSelector().text("设置"));
        set.click();
        sleep(200);

        /* 退出登录 */
        UiScrollable setitems = new UiScrollable(new UiSelector().resourceId("com.jifen.qukan:id/ad"));
        setitems.flingForward();
        setitems.flingForward();

        UiObject quit = new UiObject(new UiSelector().text("退出登录"));
        quit.click();
        sleep(200);
    }

    public void doRecieve50() throws UiObjectNotFoundException {
        /* 领取50金币 */
        UiObject receive50 = new UiObject(new UiSelector().resourceId("com.jifen.qukan:id/tn"));
        receive50.click();
        sleep(200);
        try {
            UiObject iknow = new UiObject(new UiSelector().text("我知道了"));
            iknow.click();
            sleep(200);
        } catch (Exception e) {
            Log.d(TAG, "qrs : " + e);
        }
    }

    public void doNews() throws UiObjectNotFoundException {
        /* 头条 */
        UiCollection bottomTabs = new UiCollection(new UiSelector().resourceId("com.jifen.qukan:id/tabs"));
        UiObject news = bottomTabs.getChildByText(new UiSelector().className("android.widget.TextView"), "头条");
        news.click();
        sleep(200);
        /* UiScrollable items = new UiScrollable(new UiSelector().resourceId("android:id/list"));
         * UiObject first = items.getChild(new UiSelector().index(0));
         * first.click(); */
    }

    public void doEntertainment(int loop) throws UiObjectNotFoundException {
        /* 娱乐 */
        UiCollection newsTabs = new UiCollection(new UiSelector().resourceId("com.jifen.qukan:id/tv"));
        UiObject entertainment = newsTabs.getChildByText(new UiSelector().className("android.widget.TextView"), "娱乐");
        entertainment.click();
        sleep(1000);

        while (loop-- > 0) {
            Log.d(TAG, "qrs doEntertainment: loop = " + loop);

            try {
                UiScrollable items = new UiScrollable(new UiSelector().resourceId("com.jifen.qukan:id/th"));
                items.flingBackward();
                UiObject first = items.getChild(new UiSelector().index(0));
                first.click();
                sleep(1000);
            } catch (UiObjectNotFoundException e) {
                mDevice.pressBack();
                sleep(1000);
                continue;
            }

            try {
                UiScrollable ni = new UiScrollable(new UiSelector().resourceId("com.jifen.qukan:id/ni"));
                UiObject e1 = ni.getChild(new UiSelector().index(0));
                e1.click();
                sleep(1000);
                try {
                    UiScrollable webpage = new UiScrollable(new UiSelector().resourceId("com.jifen.qukan:id/ku"));
                    for (int i = 0; i < 4; ++i) {
                        webpage.flingForward();
                        sleep(4000);
                        webpage.flingForward();
                        sleep(4000);
                        webpage.flingBackward();
                        sleep(4000);
                        webpage.flingBackward();
                        sleep(4000);
                    }
                    UiObject back = new UiObject(new UiSelector().resourceId("com.jifen.qukan:id/fp"));
                    back.click();
                    sleep(1000);
                } catch (UiObjectNotFoundException e) {
                    UiObject close = new UiObject(new UiSelector().resourceId("com.jifen.qukan:id/i0"));
                    close.click();
                    sleep(1000);
                }
            } catch (UiObjectNotFoundException e) {
                sleep(1000);
                mDevice.pressBack();
                sleep(1000);
            }
        }
    }

    public void doTask() throws UiObjectNotFoundException {
        /* 底部的任务 */
        UiObject task = new UiObject(new UiSelector().text("任务"));
        task.click();
        sleep(1000);

        UiObject toutiao = new UiObject(new UiSelector().resourceId("com.jifen.qukan:id/jx"));
        toutiao.click();
        sleep(1000);
        
        /* Sign */
        // UiObject sign = new UiObject(new UiSelector().resourceId("com.jifen.qukan:id/sign_btn_container"));
        // sign.click();
        // sleep(1000);

        // UiScrollable taskItems = new UiScrollable(new UiSelector().resourceId("com.jifen.qukan:id/task_scroll"));
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
            UiCollection newsTabs = new UiCollection(new UiSelector().resourceId("com.jifen.qukan:id/tab_news"));
            UiObject video = newsTabs.getChildByText(new UiSelector().className("android.widget.TextView"), "视频");
            video.click();
            sleep(30000);
            mDevice.pressBack();
        }
        // while (loop-- > 0) {
        //     UiScrollable items = new UiScrollable(new UiSelector().resourceId("com.jifen.qukan:id/listview"));
        //     items.scrollForward();
        //     UiObject first = items.getChild(new UiSelector().index(0));
        //     first.click();
        //     sleep(30000);
        //     mDevice.pressBack();
        // }
    }
}