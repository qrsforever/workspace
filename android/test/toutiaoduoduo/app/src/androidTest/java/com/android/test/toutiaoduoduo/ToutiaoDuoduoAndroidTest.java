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

public class ToutiaoDuoduoAndroidTest extends UiAutomatorTestCase {

    public static final String TAG = ToutiaoDuoduoAndroidTest.class.getSimpleName();
    public UiDevice mDevice = null;
    public static int mLoopCount = 24;
    public static int mNewsCount = 14;

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
            sleep(6000);
        } catch (Exception e) {
            Log.d(TAG, "qrs start lite activity error: " + e);
        }
    }

    public void doEntertainment(int loop) throws UiObjectNotFoundException {
        try {
            UiObject task2 = new UiObject(new UiSelector().text("首页"));
            task2.click();
            sleep(1000);
        } catch (Exception e) {
            try {
                Log.d(TAG, "qrs error: " + e);
                mDevice.executeShellCommand("am start -n  com.lite.infoflow/com.lite.infoflow.launcher.LauncherActivity");
                sleep(6000);
                UiObject task2 = new UiObject(new UiSelector().text("首页"));
                task2.click();
                sleep(1000);
            } catch (Exception e1) {
                Log.d(TAG, "qrs error: " + e1);
            }
        }
        while (loop-- > 0) {
            try {
                Log.d(TAG, "qrs doEntertainment: loop = " + loop);
                /* 娱乐 */
                try {
                    UiObject task = new UiObject(new UiSelector().text("首页"));
                    task.click();
                    sleep(1000);
                } catch (Exception e1) {
                    Log.d(TAG, "qrs error: " + e1);
                    mDevice.pressBack();
                    mDevice.pressBack();
                }

                UiObject et = new UiObject(new UiSelector().text("推荐"));
                et.click();
                sleep(1000);
                mDevice.executeShellCommand("input swipe 350 400 350 750 800");
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
        try {
            UiObject task = new UiObject(new UiSelector().text("赚钱"));
            task.click();
            sleep(1000);
            mDevice.executeShellCommand("input tap 650 80");
            mDevice.pressBack();
        } catch (Exception e) {
            Log.d(TAG, "qrs error: " + e);
        }

        UiObject task2 = new UiObject(new UiSelector().text("首页"));
        task2.click();
        sleep(1000);

        for (int i = 0; i < 30; ++i) {
            try {
                UiObject so1 = new UiObject(new UiSelector().text("搜索或输入网址"));
                so1.click();
                sleep(200);

                /* 撸搜索(主动) */
                if (i < 7) {
                    try {
                        int idx = new Random().nextInt(mSoso.length);
                        UiObject so2 = new UiObject(new UiSelector().text("搜你想搜的"));
                        so2.setText(mSoso[idx]);
                        sleep(200);
                        UiObject so3 = new UiObject(new UiSelector().text("搜索"));
                        so3.click();
                        sleep(1000);
                    } catch (Exception e) {
                        Log.d(TAG, "qrs error: " + e);
                        mDevice.pressBack();
                        continue;
                    }
                }

                /* 撸搜索(热点) */
                if (i > 6) {
                    try {
                        mDevice.executeShellCommand("input tap 350 350");
                        sleep(1000);
                    } catch (Exception e) {
                        Log.d(TAG, "qrs error: " + e);
                        mDevice.pressBack();
                        continue;
                    }
                }

                try {
                    for (int j = 0; j < 3; ++j) {
                        mDevice.executeShellCommand("input swipe 350 950 350 250 1000");
                        sleep(1000);
                    }
                    mDevice.executeShellCommand("input tap 350 350");
                    sleep(1000);
                    for (int j = 0; j < 5; ++j) {
                        mDevice.executeShellCommand("input swipe 350 950 350 250 1000");
                        sleep(1000);
                    }
                } catch (Exception e) {
                    Log.d(TAG, "qrs error: " + e);
                }
                mDevice.pressBack();
                mDevice.pressBack();
                mDevice.pressBack();
            } catch (Exception e) {
                Log.d(TAG, "qrs error: " + e);
                try {
                    mDevice.executeShellCommand("am start -n  com.lite.infoflow/com.lite.infoflow.launcher.LauncherActivity");
                    sleep(4000);
                } catch (Exception e1) {
                    Log.d(TAG, "qrs error: " + e1);
                }
            }
        }
    }
}
