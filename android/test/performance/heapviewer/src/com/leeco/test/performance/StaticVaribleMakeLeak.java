package com.leeco.test.performance;

import android.app.Activity;
import android.os.Bundle;
import android.widget.TextView;

public class StaticVaribleMakeLeak extends Activity {

    public static final String TAG = StaticVaribleMakeLeak.class.getSimpleName();

    private static TextView mTV = null;

    @SuppressWarnings("unused")
    private int[] mBigData_i = new int[3 * 1024 * 1024]; // 验证Activity没有GC掉

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.static_varible);

        // mTV是今天变量生命周期和应用程序相同， 内部含有StaticVaribleMakeLeak指针, 导致无法释放
        // 再次调用new TextView(this)才能GC掉上次的Activity， 但是这次的又不能GC。
        mTV = new TextView(this); 
        mTV.setText("Hello");
    }
}
