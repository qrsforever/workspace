package com.android.test.cashtoutiao;

import android.util.Log;
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

import android.graphics.Rect;
import org.junit.Test;
import java.util.List;
import java.util.Random;

public class CashToutiaoAndroidTest extends UiAutomatorTestCase {

    public static final String TAG = CashToutiaoAndroidTest.class.getSimpleName();
    public UiDevice mDevice = null;
    public static final int mLoopCount = 3;
    public static final int mNewsCount = 16;
    public static final int mVideoCount = 6;
    public static final int mPhoneType = 2; // 1: leshi 2: xiaomi
    public static int mHeight = 1920;
    public static int mWidth = 1280;

    public static final String[] mSoso = {
        "李宇春","张靓颖","周笔畅","何洁","刘亦菲","张含韵","陈好","尚雯婕",
        "汤唯","张筱雨","韩雪","孙菲菲","张嘉倪","霍思燕","陈紫函","朱雅琼",
        "江一燕","厉娜","许飞","胡灵","郝菲尔","刘力扬","reborn","章子怡",
        "谭维维","魏佳庆","张亚飞","李旭丹","孙艺心","巩贺","艾梦萌","闰妮",
        "王蓉","汤加丽","汤芳","牛萌萌","范冰冰","赵薇","周迅","金莎",
        "纪敏佳","黄雅莉","叶一茜","马苏","阿桑","董卿","金铭","徐行",
        "姚笛","朱妍","夏颖","陈西贝","冯家妹","高娅媛","林爽","郑靖文",
        "陶虹","徐静蕾","黄奕","董洁","巩俐","高圆圆","于娜","孟广美",
        "Gameapple","美女奉奉","小龙女彤彤","张子萱","果子","丁贝莉","吸血芭比","公交MM",
        "香香","段思思","二月丫头","刘羽琦","dodolook","拉拉公主","沈丽君","周璟馨",
        "丁叮","谢雅雯","陈嘉琪","宋琳","郭慧敏","卢洁云","佘曼妮","黄景",
        "马艳丽","蒋雯丽","宁静","许晴","张静初","瞿颖","张延","孙俪",
        "闵春晓","蔡飞雨","邓莎","白冰","程媛媛","吴婷","殷叶子","朱伟珊",
        "孙菂","赵梦恬","龚洁","许晚秋","杨舒婷","乔维怡","王海珍","易慧",
        "谢雨欣","陈娟红","舒畅","李小璐","曹颖","李冰冰","王艳","沈星",
        "阿朵","周洁","杨林","李霞","陈自瑶","李小冉","李湘","金巧巧",
        "蒋勤勤","梅婷","刘涛","秦海璐","安又琪","杨钰莹","马伊俐","陈红",
        "鲍蕾","牛莉","胡可","杨幂","龚蓓苾","田震","杨童舒","吕燕",
        "王姬","苗圃","李欣汝","王小丫","秦岚","徐帆","刘蓓","彭心怡",
        "邓婕","眉佳","李媛媛","刘晓庆","杨若兮","黄圣依","林熙","薛佳凝",
        "斯琴格日乐","宋祖英","郝蕾","乐珈彤","冯婧","宋丹丹","盖丽丽","田海蓉",
        "杨澜","沈冰","王宇婕","王希维","姜培琳","何晴","焦媛","白灵",
        "胡静","陈冲","刘怡君","韦唯","龚雪","周彦宏","刘丹","傅艺伟",
        "谢东娜","朱媛媛","黑鸭子","周璇","吕丽萍","杨欣","陈小艺","伍宇娟",
        "苏瑾","李玲玉","张凯丽","潘虹","沈丹萍","岳红","赵静怡","宋晓英"
    };


    @Override
    protected void setUp() throws Exception {
        super.setUp();
        mDevice = UiDevice.getInstance(getInstrumentation());
        mHeight = mDevice.getDisplayHeight();
        mWidth = mDevice.getDisplayWidth();
    }

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

           // try {
           //     if (flag == 0) {
           //         if (i < mLoopCount / 2) {
           //             Log.d(TAG, "qrs Login 188");
           //             if (doLogin("18811165327", "ting1412") < 0) {
           //                 Log.d(TAG, "qrs swtich Login 158");
           //                 doLogin("15801310416", "20150505");
           //             }
           //         } else {
           //             Log.d(TAG, "qrs Login 158");
           //             if (doLogin("15801310416", "20150505") < 0) {
           //                 Log.d(TAG, "qrs swtich Login 188");
           //                 doLogin("18811165327", "ting1412");
           //             }
           //         }
           //     }
           // } catch (UiObjectNotFoundException e) {
           //     Log.d(TAG, "qrs : " + e);
           // }

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
                Log.d(TAG, "Do Entertainment");
                doEntertainment(mNewsCount);
            } catch (UiObjectNotFoundException e) {
                Log.d(TAG, "qrs : " + e);
            }

            try {
                Log.d(TAG, "Do Video");
                doVideo(mVideoCount);
            } catch (UiObjectNotFoundException e) {
                Log.d(TAG, "qrs : " + e);
            }


            // if (i == mLoopCount / 2) {
            //     try {
            //         Log.d(TAG, "Logout");
            //         doLogout();
            //     } catch (UiObjectNotFoundException e) {
            //         Log.d(TAG, "qrs : " + e);
            //     }
            //     flag = 0;
            // }
        }

        // try {
        //     Log.d(TAG, "qrs end Logout");
        //     doLogout();
        // } catch (UiObjectNotFoundException e) {
        //     Log.d(TAG, "qrs : " + e);
        // }
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
                sleep(5000);
                mDevice.pressBack();
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
        mDevice.pressBack();
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
            try {
                try {
                    UiScrollable items = new UiScrollable(new UiSelector().resourceId("android:id/list"));
                    items.flingBackward();
                    UiObject first = items.getChild(new UiSelector().index(0));
                    first.click();
                    sleep(1000);
                } catch (UiObjectNotFoundException e) {
                    Log.d(TAG, "qrs not found list: " + e);
                    mDevice.pressBack();
                    continue;
                }

                UiScrollable webpage = new UiScrollable(new UiSelector().resourceId("com.cashtoutiao:id/web_layout"));

                int lcnt = new Random().nextInt(3) + 3;
                for (int i = 0; i < lcnt; ++i) {
                    webpage.flingForward();
                    sleep(2000);
                    webpage.flingForward();
                    sleep(2000);
                    webpage.flingBackward();
                    sleep(2000);
                }
                if (loop % 7 == 0) {
                    _Input_Tap(1280 - 60, 1920 - 60);
                    Thread.sleep(300);
                    /* 分享 */
                    UiObject2 qq = mDevice.findObject(By.text("QQ好友"));
                    qq.click();
                    // Rect r = qq.getVisibleBounds();
                    // _Input_Tap(r.left + 100, r.top - 100);
                    Thread.sleep(2000);

                    UiObject2 lu = mDevice.findObject(By.text("撸世界"));
                    lu.click();
                    Thread.sleep(1000);
                    UiObject2 luto = mDevice.findObject(By.res("com.tencent.mobileqq:id/dialogRightBtn"));
                    luto.click();
                    Thread.sleep(3000);
                    UiObject2 lugo = mDevice.findObject(By.res("com.tencent.mobileqq:id/dialogRightBtn"));
                    lugo.click();
                    Thread.sleep(2000);
                    _Input_Tap(600, 1500);
                    Thread.sleep(5000);
                    _Input_Swipe(360, 1280, 360, 800, 200);
                    Thread.sleep(300);
                    mDevice.pressBack();
                    Thread.sleep(300);
                    mDevice.pressBack();
                    Thread.sleep(300);
                    mDevice.pressBack();
                    Thread.sleep(300);
                }
                UiObject back = new UiObject(new UiSelector().resourceId("com.cashtoutiao:id/iv_back"));
                back.click();
                sleep(200);
            } catch (Exception en) {
                Log.d(TAG, "qrs entertainment: e = " + en); 
            }
        }
    }

    public void doTask() throws UiObjectNotFoundException {
        /* 底部的任务 */
        // UiCollection bottomTabs = new UiCollection(new UiSelector().resourceId("com.cashtoutiao:id/tabs"));
        // UiObject task = bottomTabs.getChildByText(new UiSelector().className("android.widget.TextView"), "任务中心");
        mDevice.pressBack();
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
        }

        try {
            _Input_Swipe(360, 1280, 360, 300, 200);
            Thread.sleep(300);
        } catch (Exception e) {
        }

        /* 阅读资讯5分钟 */
        try {
            UiObject2 r2o = mDevice.findObject(By.text("每天阅读资讯可获得额外奖励"));
            UiObject2 r2o_p = r2o.getParent(); 
            List<UiObject2> childList = r2o_p.getChildren();
            if (childList.size() == 3) {
                UiObject2 r3o = childList.get(2);
                if (r3o.getText().equals("立即领取"))
                    r3o.click();
            }
        } catch (Exception r2o_e) {
            Log.d(TAG, "qrs doTask news: e = " + r2o_e); 
        }

        /* 观看视频5分钟 */
        try {
            UiObject2 v2o = mDevice.findObject(By.text("进入视频详情页，观看视频可获得额外奖励"));
            UiObject2 v2o_p = v2o.getParent(); 
            List<UiObject2> childList = v2o_p.getChildren();
            if (childList.size() == 3) {
                UiObject2 v3o = childList.get(2);
                if (v3o.getText().equals("立即领取"))
                    v3o.click();
            }
        } catch (Exception v2o_e) {
            Log.d(TAG, "qrs doTask video: e = " + v2o_e); 
        }

        /* 新闻搜索, 赚金币 */
        try {
            UiObject2 n2o = mDevice.findObject(By.text("新闻搜索，赚金币"));
            n2o.click();
            _Input_Swipe(360, 1280, 360, 800, 200);
            Thread.sleep(300);
            UiObject2 s2o = mDevice.findObject(By.text("立即搜索"));
            s2o.click();
            Thread.sleep(1000);
            for (int i = 0; i < 2; ++i) {
                UiObject2 s2e = mDevice.findObject(By.res("com.cashtoutiao:id/search_content"));
                s2e.setText(mSoso[new Random().nextInt(mSoso.length)]);
                Thread.sleep(1000);
                UiObject2 s2b = mDevice.findObject(By.res("com.cashtoutiao:id/search_btn"));
                s2b.click();
                Thread.sleep(1000);
                _Input_Tap(mWidth/2, mWidth/2);
                Thread.sleep(1000);
                for (int j = 0; j < 8; ++j) {
                    _Input_Swipe(360, 1280, 360, 800, 200);
                    Thread.sleep(2000);
                }
                mDevice.pressBack();
                mDevice.pressBack();
            }
        } catch (Exception n2o_e) {
            Log.d(TAG, "qrs doTask: e search = " + n2o_e); 
        }



        // try {
        //     UiScrollable items = new UiScrollable(new UiSelector().resourceId("com.cashtoutiao:id/add_daily_task"));
        //     UiObject ro = items.getChild(new UiSelector().index(6));
        // } catch (UiObjectNotFoundException task_e) {
        //     Log.d(TAG, "qrs doTask: e = " + task_e); 
        //     return;
        // }
        
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
        mDevice.pressBack();
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
