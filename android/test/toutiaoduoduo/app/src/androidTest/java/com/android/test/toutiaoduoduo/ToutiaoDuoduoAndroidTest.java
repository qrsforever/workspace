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

    public static final String TAG = ToutiaoDuoduoAndroidTest.class.getSimpleName() + " qrs";
    public UiDevice mDevice = null;
    public static int mHeight = 1920;
    public static int mWidth = 1280;

    public static int mLoopCount = 2;
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
        mHeight = mDevice.getDisplayHeight();  
        mWidth = mDevice.getDisplayWidth(); 
    }

    @Test
    public void testDemo() throws UiObjectNotFoundException {
        int i, flag = 0;
        for (i = 0; i < mLoopCount; ++i) {
            try {
                Log.d(TAG, "qrs Start anttoutiao + i = " + i);
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
                _Input_Swipe(620, 720, 620, 1350, 800);
                sleep(1000);
                _Input_Tap(620, 620);
                sleep(3000);
                for (int i = 0; i < 6; ++i) {
                    _Input_Swipe(620, 1125, 620, 450, 1000);
                    sleep(2000);
                }
                mDevice.pressBack();
            } catch (Exception e) {
                Log.d(TAG, "qrs error: " + e);
            }
        }
        mDevice.pressBack();
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

    public void doTask() throws UiObjectNotFoundException {
        /* 底部的任务 */
        try {
            UiObject task = new UiObject(new UiSelector().text("赚钱"));
            task.click();
            sleep(1000);
            _Input_Tap(1150, 140);
            sleep(3000);
            _Input_Tap(900, 590);
            mDevice.pressBack();
        } catch (Exception e) {
            Log.d(TAG, "qrs error: " + e);
        }

        UiObject task2 = new UiObject(new UiSelector().text("首页"));
        task2.click();
        sleep(1000);

        for (int i = 0; i < 15; ++i) {
            try {
                UiObject so1 = new UiObject(new UiSelector().text("搜索或输入网址"));
                so1.click();
                sleep(200);

                /* 撸搜索(主动) */
                if (i < 2) {
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
                if (i >= 2) {
                    try {
                        _Input_Tap(620, 620);
                        sleep(1000);
                    } catch (Exception e) {
                        Log.d(TAG, "qrs error: " + e);
                        mDevice.pressBack();
                        continue;
                    }
                }

                try {
                    for (int j = 0; j < 3; ++j) {
                        _Input_Swipe(620, 1690, 620, 480, 1000);
                        sleep(1000);
                    }
                    _Input_Tap(620, 620);
                    sleep(1000);
                    for (int j = 0; j < 5; ++j) {
                        _Input_Swipe(620, 1690, 620, 480, 1000);
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
