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

    @Override
    protected void setUp() throws Exception {
        super.setUp();
        UiDevice device = getUiDevice();
        device.executeShellCommand("am force-stop com.cashtoutiao");
        device.pressHome();
        UiObject allAppsButton = new UiObject(new UiSelector().description("Apps"));
        allAppsButton.clickAndWaitForNewWindow();
        UiObject toutiao = new UiObject(new UiSelector().text("惠头条"));
        toutiao.click();
        sleep(3000);
    }

    @Test
    public void testDemo() throws UiObjectNotFoundException {
        try {
            doRecieve50();
        } catch (UiObjectNotFoundException e) {
        }

        try {
            doNews();
            doEntertainment();
        } catch (UiObjectNotFoundException e) {
        }

        try {
            doVideo();
        } catch (UiObjectNotFoundException e) {
        }
    }

    public void doRecieve50() throws UiObjectNotFoundException {
        /* 领取50金币 */
        UiObject receive50 = new UiObject(new UiSelector().resourceId("com.cashtoutiao:id/yes_receive_layout"));
        receive50.click();
        sleep(1000);
    }

    public void doNews() throws UiObjectNotFoundException {
        /* 头条 */
        UiCollection bottomTabs = new UiCollection(new UiSelector().resourceId("com.cashtoutiao:id/tabs"));
        UiObject news = bottomTabs.getChildByText(new UiSelector().className("android.widget.TextView"), "头条");
        news.click();
        sleep(1000);
        /* UiScrollable items = new UiScrollable(new UiSelector().resourceId("android:id/list"));
         * UiObject first = items.getChild(new UiSelector().index(0));
         * first.click(); */
    }

    public void doEntertainment() throws UiObjectNotFoundException {
        /* 娱乐 */
        UiCollection newsTabs = new UiCollection(new UiSelector().resourceId("com.cashtoutiao:id/tab_news"));
        UiObject entertainment = newsTabs.getChildByText(new UiSelector().className("android.widget.TextView"), "娱乐");
        entertainment.click();
        sleep(1000);

        UiScrollable items = new UiScrollable(new UiSelector().resourceId("android:id/list"));
        UiObject first = items.getChild(new UiSelector().index(0));
        first.click();
        sleep(1000);

        int i = 0;
        UiScrollable webpage = new UiScrollable(new UiSelector().resourceId("com.cashtoutiao:id/web_layout"));
        while (i++ < 30) {
            webpage.flingForward();
            sleep(1000);
            webpage.flingForward();
            sleep(1000);
            webpage.flingBackward();
            sleep(1000);
            webpage.flingBackward();
            sleep(1000);
        }
        UiObject back = new UiObject(new UiSelector().resourceId("com.cashtoutiao:id/iv_back"));
        back.click();
        sleep(1000);
    }

    public void doVideo() throws UiObjectNotFoundException {
        /* 底部的视频 */
        UiCollection bottomTabs = new UiCollection(new UiSelector().resourceId("com.cashtoutiao:id/tabs"));
        UiObject video = bottomTabs.getChildByText(new UiSelector().className("android.widget.TextView"), "视频");
        video.click();
        sleep(1000);
    }

    public void doTask() throws UiObjectNotFoundException {
        /* 底部的任务 */
        UiCollection bottomTabs = new UiCollection(new UiSelector().resourceId("com.cashtoutiao:id/tabs"));
        UiObject task = bottomTabs.getChildByText(new UiSelector().className("android.widget.TextView"), "任务中心");
        task.click();
        sleep(1000);
    }
}
