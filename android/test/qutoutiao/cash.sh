while ((1))
do
    adb shell am instrument -w com.android.test.qutoutiao.test/android.support.test.runner.AndroidJUnitRunner
    sleep 3
done
