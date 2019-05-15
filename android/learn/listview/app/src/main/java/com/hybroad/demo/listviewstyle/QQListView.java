package com.hybroad.demo.listviewstyle;
import android.content.Context;
import android.util.AttributeSet;
import android.view.MotionEvent;
import android.widget.ListView;
import android.widget.Toast;

public class QQListView extends ListView {
    Context mContext;
    public QQListView(Context context, AttributeSet attrs) {
        super(context, attrs);
        mContext = context;
    }
    @Override
    public boolean onTouchEvent(MotionEvent ev) {
        return super.onTouchEvent(ev);
    }
}
