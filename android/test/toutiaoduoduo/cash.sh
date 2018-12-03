while ((1))
do
    adb shell am instrument -w com.android.test.toutiaoduoduo.test/android.support.test.runner.AndroidJUnitRunner
    sleep 3
done
