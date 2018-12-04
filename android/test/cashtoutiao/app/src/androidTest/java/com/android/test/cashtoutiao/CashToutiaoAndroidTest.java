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
    public static final int mLoopCount = 8;
    public static final int mNewsCount = 8;
    public static final int mVideoCount = 4;
    public static final int mPhoneType = 2; // 1: leshi 2: xiaomi

    @Override
    protected void setUp() throws Exception {
        super.setUp();
        mDevice = getUiDevice();
    }

    @Test
    public void testDemo() throws UiObjectNotFoundException {
        int i, flag = 0;
        for (i = 0; i < mLoopCount; ++i) {
            Log.d(TAG, "qrs testDemo: i = " + i);
            try {
                Log.d(TAG, "qrs Start CashToutiao");
                doStartApp();
            } catch (UiObjectNotFoundException e) {
                Log.d(TAG, "qrs : " + e);
            }

            try {
                if (flag == 0) {
                    if (i < mLoopCount / 2) {
                        Log.d(TAG, "qrs Login 188");
                        if (doLogin("18811165327", "ting1412") < 0) {
                            Log.d(TAG, "qrs swtich Login 158");
                            doLogin("15801310416", "20150505");
                        }
                    } else {
                        Log.d(TAG, "qrs Login 158");
                        if (doLogin("15801310416", "20150505") < 0) {
                            Log.d(TAG, "qrs swtich Login 188");
                            doLogin("18811165327", "ting1412");
                        }
                    }
                }
            } catch (UiObjectNotFoundException e) {
                Log.d(TAG, "qrs : " + e);
            }

            try {
                Log.d(TAG, "qrs Close AD");
                doCloseAD();
            } catch (UiObjectNotFoundException e) {
                Log.d(TAG, "qrs qrs : " + e);
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

            try {
                Log.d(TAG, "Do Video");
                doVideo(mVideoCount);
            } catch (UiObjectNotFoundException e) {
                Log.d(TAG, "qrs : " + e);
            }

            try {
                Log.d(TAG, "Do Entertainment");
                doEntertainment(mNewsCount);
            } catch (UiObjectNotFoundException e) {
                Log.d(TAG, "qrs : " + e);
            }

            if (i == mLoopCount / 2) {
                try {
                    Log.d(TAG, "Logout");
                    doLogout();
                } catch (UiObjectNotFoundException e) {
                    Log.d(TAG, "qrs : " + e);
                }
                flag = 0;
            }
        }

        try {
            Log.d(TAG, "qrs end Logout");
            doLogout();
        } catch (UiObjectNotFoundException e) {
            Log.d(TAG, "qrs : " + e);
        }
    }

    public void doClearApps() throws UiObjectNotFoundException {
        try {
            try {
                // android4.4 or below, perhaps no permission
                if (mPhoneType == 2)
                    mDevice.executeShellCommand("am force-stop com.cashtoutiao");
                else
                    Runtime.getRuntime().exec("am force-stop com.cashtoutiao");
            } catch (Exception e) {
                // android5.0 or above
                mDevice.executeShellCommand("am force-stop com.cashtoutiao");
            }
            Log.d(TAG, "Press Pecent apps");
            mDevice.pressRecentApps();
            sleep(200);
        } catch (Exception e) {
        }
        UiScrollable allApps = new UiScrollable(new UiSelector().resourceId("com.android.systemui:id/recents_container"));
        UiObject app = allApps.getChild(new UiSelector().description("惠头条"));
        if (app.exists()) {
            app.swipeLeft(10);
            sleep(200);
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

        Log.d(TAG, "qrs PhoneType: " + mPhoneType);
        // 乐视手机
        if (mPhoneType == 1) {
            UiObject toutiao = new UiObject(new UiSelector().text("惠头条"));
            toutiao.click();
            sleep(1000);
        } else if(mPhoneType == 2) {
            // 红米手机
            try {
                mDevice.executeShellCommand("am start -n com.cashtoutiao/com.cashtoutiao.common.ui.SplashActivity");
                sleep(1000);
                return;
            } catch (Exception e) {
                Log.d(TAG, "qrs start cashtoutiao activity error: " + e);
            }
        }
    }

    public void doCloseAD() throws UiObjectNotFoundException {
        // 关闭广告
        try {
            UiObject closeAD = new UiObject(new UiSelector().resourceId("com.cashtoutiao:id/img_close"));
            closeAD.click();
            sleep(200);
        } catch (UiObjectNotFoundException e) {
            Log.d(TAG, "qrs : " + e);
        }
        // 关闭升级
        try {
            UiObject not = new UiObject(new UiSelector().text("以后再说"));
            not.click();
            sleep(200);
        } catch (UiObjectNotFoundException e) {
            Log.d(TAG, "qrs : " + e);
        }
    }

    public int doLogin(String u, String c) throws UiObjectNotFoundException {
        /* 登录 */
        try {
            UiObject user = new UiObject(new UiSelector().resourceId("com.cashtoutiao:id/username"));
            user.setText(u);
            UiObject pass = new UiObject(new UiSelector().resourceId("com.cashtoutiao:id/password"));
            pass.setText(c);
            UiObject login = new UiObject(new UiSelector().resourceId("com.cashtoutiao:id/login_button"));
            login.click();
            sleep(5000);
        } catch (UiObjectNotFoundException e) {
            Log.d(TAG, "qrs already login: " + e);
            return 0;
        }

        /* 再次查询布局, 确保正常登录 */
        try {
            UiObject user = new UiObject(new UiSelector().resourceId("com.cashtoutiao:id/username"));
            user.setText(u);
            return -1;
        } catch (UiObjectNotFoundException e) {
            Log.d(TAG, "qrs login success: " + e);
            return 0;
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
        try {
            UiObject receive50 = new UiObject(new UiSelector().resourceId("com.cashtoutiao:id/yes_receive_layout"));
            receive50.click();
            sleep(200);
        } catch (UiObjectNotFoundException e) {
            Log.d(TAG, "qrs : " + e);
            return;
        }

        try {
            UiObject ignore = new UiObject(new UiSelector().text("忽略"));
            ignore.click();
        } catch (UiObjectNotFoundException e) {
            Log.d(TAG, "qrs : " + e);
        }
    }

    public void doEntertainment(int loop) throws UiObjectNotFoundException {
        /* 点击头条栏 */
        try {
            UiObject news = new UiObject(new UiSelector().text("头条"));
            news.click();
            sleep(200);
            /* 娱乐 */
            UiObject entertainment = new UiObject(new UiSelector().text("娱乐"));
            entertainment.click();
            sleep(200);
        } catch (UiObjectNotFoundException e) {
            Log.d(TAG, "qrs : " + e);
        }

        while (loop-- > 0) {
            Log.d(TAG, "qrs doEntertainment: loop = " + loop); 
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
            sleep(200);
        }
    }

    public void doTask() throws UiObjectNotFoundException {
        /* 底部的任务 */
        // UiCollection bottomTabs = new UiCollection(new UiSelector().resourceId("com.cashtoutiao:id/tabs"));
        // UiObject task = bottomTabs.getChildByText(new UiSelector().className("android.widget.TextView"), "任务中心");
        try {
            UiObject task = new UiObject(new UiSelector().text("任务中心"));
            task.click();
        } catch (UiObjectNotFoundException e) {
            Log.d(TAG, "qrs doTask: e = " + e); 
            return;
        }

        /* Sign */
        try {
            Log.d(TAG, "qrs sign");
            UiObject sign = new UiObject(new UiSelector().resourceId("com.cashtoutiao:id/sign_btn_container"));
            sign.click();
        } catch (UiObjectNotFoundException e) {
            Log.d(TAG, "qrs doTask: e = " + e); 
            return;
        }

        // UiScrollable taskItems = new UiScrollable(new UiSelector().resourceId("com.cashtoutiao:id/task_scroll"));

        /* news */
        // try {
        //     Log.d(TAG, "qrs cash news");
        //     UiObject newsTask = new UiObject(new UiSelector().textMatches("^阅读资讯.*"));
        //     taskItems.scrollIntoView(newsTask);
        //     newsTask.click();
        //     sleep(1000);
        //     UiObject getNewsCash = new UiObject(new UiSelector().text("立即领取"));
        //     getNewsCash.click();
        // } catch (UiObjectNotFoundException e) {
        //     Log.d(TAG, "qrs doTask: e = " + e); 
        //     return;
        // }

        // /* Video */
        // try {
        //     Log.d(TAG, "qrs cash video");
        //     UiScrollable taskItems = new UiScrollable(new UiSelector().resourceId("com.cashtoutiao:id/task_scroll"));
        //     UiObject videoTask = new UiObject(new UiSelector().textMatches("^观看视频.*"));
        //     taskItems.scrollIntoView(videoTask);
        //     videoTask.click();
        //     sleep(1000);
        //     UiObject getVideoCash = new UiObject(new UiSelector().text("立即领取"));
        //     getVideoCash.click();
        // } catch (UiObjectNotFoundException e) {
        //     Log.d(TAG, "qrs doTask: e = " + e); 
        //     return;
        // }
    }

    public void doVideo(int loop) throws UiObjectNotFoundException {
        /* 视频 */
        try {
            UiObject video = new UiObject(new UiSelector().text("视频"));
            video.click();
            sleep(200);
            while (loop-- > 0) {
                Log.d(TAG, "qrs doVideo: loop = " + loop); 
                UiScrollable items = new UiScrollable(new UiSelector().resourceId("com.cashtoutiao:id/listview"));
                items.scrollForward();
                UiObject first = items.getChild(new UiSelector().index(1));
                first.click();
                sleep(32000);
                mDevice.pressBack();
            }
        } catch (UiObjectNotFoundException e) {
            Log.d(TAG, "qrs doVideo: e = " + e); 
        } 
    }
}
