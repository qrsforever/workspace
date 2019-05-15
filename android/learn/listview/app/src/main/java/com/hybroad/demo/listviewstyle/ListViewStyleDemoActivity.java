package com.hybroad.demo.listviewstyle;

import java.util.ArrayList;
import java.util.HashMap;

import android.app.Activity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.AdapterView;
import android.widget.AdapterView.OnItemClickListener;
import android.widget.Button;
import android.widget.ListView;
import android.widget.SimpleAdapter;
public class ListViewStyleDemoActivity extends Activity {

    static private final String TAG = "Hybroad-ListViewStyleDemoActivity";
    private Button mbtn_add_item = null;

    private ArrayList<HashMap<String, Object>> mlist_items = null;
    private SimpleAdapter mlist_items_adapter = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        Log.d(TAG, "onCreate " + this.hashCode());
        super.onCreate(savedInstanceState);
        this.setContentView(R.layout.main);

        mbtn_add_item = (Button)this.findViewById(R.id.btn_add);
        mbtn_add_item.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
                HashMap<String, Object> map = new HashMap<String, Object>();
                map.put("item_image", R.drawable.checked);
                map.put("item_title", "Title-" + mlist_items.size());
                map.put("item_text", "New item!");
                mlist_items.add(map);
                mlist_items_adapter.notifyDataSetChanged();
            }
        });
        ListView list_view = (ListView)this.findViewById(R.id.list_view);
        mlist_items = new ArrayList<HashMap<String, Object>>();
        HashMap<String, Object> map = null;
        for (int i = 0; i < 50; i++) {
            map = new HashMap<String, Object>();
            map.put("item_image", R.drawable.checked);
            map.put("item_title", "Title-" + i);
            map.put("item_text", "Hello World!");
            mlist_items.add(map);
        }

        mlist_items_adapter = new SimpleAdapter(
                this, 
                mlist_items,
                R.layout.list_item,
                new String[] { "item_image", "item_title", "item_text" },
                new int[] { R.id.item_image, R.id.item_title, R.id.item_text } );

        list_view.setAdapter(mlist_items_adapter);

        list_view.setOnItemClickListener(new OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view,
                    int position, long id) {
                Log.d(TAG, "onItemClick " + this.hashCode());
                ListViewStyleDemoActivity.this.setTitle("On click " + position + " item");
            }

        });
    }
}
