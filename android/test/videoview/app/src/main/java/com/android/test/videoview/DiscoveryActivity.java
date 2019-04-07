package com.android.test.videoview;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Set;

import android.util.Log;
import android.app.ListActivity;
import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;
import android.widget.ListView;
import android.widget.SimpleAdapter;

public class DiscoveryActivity extends ListActivity {
	final static String TAG = "QRS-DiscoveryActivity";

    private ArrayList<HashMap<String, String>> list = null;
    private List<BluetoothDevice> mBondedDevices = new ArrayList<BluetoothDevice>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Log.d(TAG, "onCreate");
        setContentView(R.layout.discovery);

        list = new ArrayList<HashMap<String, String>>();

        showDevices();
    }

    public void showDevices() {
        BluetoothAdapter blueToothAdapter = BluetoothAdapter.getDefaultAdapter();
        Set<BluetoothDevice> devices = blueToothAdapter.getBondedDevices();
        Log.d(TAG, "devices.szie = " + devices.size());
        if (devices.size() > 0) {
            Iterator<BluetoothDevice> it = devices.iterator();
            BluetoothDevice bluetoothDevice = null;
            HashMap<String, String> map = new HashMap<String, String>();
            while (it.hasNext()) {
                bluetoothDevice = it.next();
                map.put("address", bluetoothDevice.getAddress());
                map.put("name", bluetoothDevice.getName());
                list.add(map);
                mBondedDevices.add(bluetoothDevice);
            }

            SimpleAdapter listAdapter = new SimpleAdapter(this, list,
                    R.layout.device, new String[] { "address", "name" },
                    new int[] { R.id.address, R.id.name });
            this.setListAdapter(listAdapter);
        }
    }

    protected void onListItemClick(ListView l, View v, int position, long id) {
        Intent result = new Intent();
        String addressStr = mBondedDevices.get(position).getAddress();
        Log.d(TAG, "addressStr = " + addressStr );
        String address = addressStr.substring(addressStr.length() - 17);

        result.putExtra("address", address);
        setResult(RESULT_OK, result);
        finish();
    }
}
