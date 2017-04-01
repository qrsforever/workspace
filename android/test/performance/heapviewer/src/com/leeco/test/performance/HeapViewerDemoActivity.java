package com.leeco.test.performance;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;

public class HeapViewerDemoActivity extends Activity implements OnClickListener {
    public static final String TAG = HeapViewerDemoActivity.class.getSimpleName();

    private Button mB1 = null;
    private Button mB2 = null;
    private Button mB3 = null;

    @SuppressWarnings("unused")
    private MyClass1 mC1 = new MyClass1(); // 占用一个class object
    @SuppressWarnings("unused")
    private MyClass2 mC2 = new MyClass2(); // 占用一个class object

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        mB1 = (Button)findViewById(R.id.inner_thread_demo);
        mB1.setOnClickListener(this);
        mB2 = (Button)findViewById(R.id.static_varible_demo);
        mB2.setOnClickListener(this);
        mB3 = (Button)findViewById(R.id.handler_class_demo);
        mB3.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
        Intent i = null;
        switch (v.getId()) {
            case R.id.inner_thread_demo:
                i = new Intent(HeapViewerDemoActivity.this, InnerThreadMakeLeak.class);
                break;

            case R.id.static_varible_demo:
                i = new Intent(HeapViewerDemoActivity.this, StaticVaribleMakeLeak.class);
                break;

            case R.id.handler_class_demo:
                i = new Intent(HeapViewerDemoActivity.this, HandlerClassMakeLeak.class);
                break;
        }
        if (i != null)
            startActivity(i);
    }
}

// see more: http://www.open-open.com/lib/view/open1481005907773.html
