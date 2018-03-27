package com.leiot.test;

import android.content.Context;
import android.util.Log;
import android.content.Intent;
import java.util.HashMap;
import java.util.Map;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import com.android.leiot.DeviceShadow;

/* TODO only for test */
public class TVDeviceShadow extends DeviceShadow {
    public static final String TAG = TVDeviceShadow.class.getSimpleName();

    private static TVDeviceShadow mDS = null;
    private Context  mContext;

    private Map<String, IOTProperty> mProperties = null;
    private Map<String, IOTCommand> mCommands = null;

    private TVDeviceShadow(Context context) {//{{{
        super("TV");
        mContext = context;
        mProperties = new HashMap<String, IOTProperty>();
        mCommands = new HashMap<String, IOTCommand>();
        iotSetup();
    }//}}}

    public int iotSetup() {//{{{
        mProperties.put(Constants.IOT_PRO_POWER,
                new Power(Constants.IOT_PRO_POWER, IOT_PROPERTY_INT32, 16));

        mProperties.put(Constants.IOT_PRO_SIGNAL,
                new Signal(Constants.IOT_PRO_SIGNAL, IOT_PROPERTY_INT32, 16));

        mProperties.put(Constants.IOT_PRO_BRIGHTNESS,
                new Brightness(Constants.IOT_PRO_BRIGHTNESS, IOT_PROPERTY_INT32, 16));

        mCommands.put(Constants.IOT_CMD_VOLUME_SWITCH, new VolumeSwitch(Constants.IOT_CMD_VOLUME_SWITCH));
        mCommands.put(Constants.IOT_CMD_CHANNEL_SWITCH, new ChannelSwitch(Constants.IOT_CMD_CHANNEL_SWITCH));
        mCommands.put(Constants.IOT_CMD_APP_START, new AppStart(Constants.IOT_CMD_APP_START));
        mCommands.put(Constants.IOT_CMD_VIDEO_SEARCH, new VideoSearch(Constants.IOT_CMD_VIDEO_SEARCH));
        mCommands.put(Constants.IOT_CMD_TEXT_PUSH, new TextPush(Constants.IOT_CMD_TEXT_PUSH));
        mCommands.put(Constants.IOT_CMD_VIDEO_PLAY, new VideoPlay(Constants.IOT_CMD_VIDEO_PLAY));

        return 0;
    }//}}}

    public static TVDeviceShadow getInstance(Context context) {//{{{
        if (mDS == null) {
            mDS = new TVDeviceShadow(context);
        }
        return mDS;
    }//}}}

    public class Power extends IOTProperty {//{{{
        public Power(String key, int type, int size) {
            super(key, type, size);
            iotFollowProperty(key, type, size);
            mVal = "1";
        }

        public String get() {
            /* TODO debug */
            Log.i(TAG, "iot---> get(" + key() + ")");
            return mVal;
        }

        public int set(String val) {
            Log.i(TAG, "iot---> set(" + key() + ", " + val);

            { // for debug
                mVal = val;
            }

            // TODO do set, get current value
            String nowVal = val;

            /* if set success, need call iotReportProperty to update itself to cloud */
            return iotReportProperty(key(), nowVal);
        }
    }//}}}

    public class Signal extends IOTProperty {//{{{
        /* TODO debug for simulation data */

        public Signal(String key, int type, int size) {
            super(key, type, size);
            iotFollowProperty(key, type, size);
            mVal = "1";
        }

        public String get() {
            Log.i(TAG, "iot---> get(" + key() + ")");
            /* TODO debug */
            return mVal;
        }

        public int set(String val) {
            Log.i(TAG, "iot---> set(" + key() + ", " + val);

            { // for debug
                mVal = val;
                updatePropertyToUI(Constants.IOT_ACTION_PRO_SIGNAL, val);
            }

            // TODO do set, get current value
            String nowVal = val;

            /* if set success, need call iotReportProperty to update itself to cloud */
            return iotReportProperty(key(), nowVal);
        }
    }//}}}

    public class Brightness extends IOTProperty {//{{{

        public Brightness(String key, int type, int size) {
            super(key, type, size);
            iotFollowProperty(key, type, size);
            mVal = "50";
        }

        public String get() {
            Log.i(TAG, "iot---> get(" + key() + ")");
            /* TODO debug */
            return mVal;
        }

        public int set(String val) {
            Log.i(TAG, "iot---> set(" + key() + ", " + val);

            { // for debug
                mVal = val;
                updatePropertyToUI(Constants.IOT_ACTION_PRO_BRIGHTNESS, val);
            }

            // TODO do set, get current value
            String nowVal = val;

            /* if set success, need call iotReportProperty to update itself to cloud */
            return iotReportProperty(key(), nowVal);
        }
    }//}}}

    public class VolumeSwitch extends IOTCommand {//{{{
        public VolumeSwitch(String key) {
            super(key);
            iotFollowCommand(key);
        }

        public int call(String params) {
            Log.i(TAG, "iot---> " + name() + "( " + params + ")");

            { // for debug
                updatePropertyToUI(Constants.IOT_CMD_VOLUME_SWITCH, params);
            }
            return 0;
        }
    }//}}}

    public class ChannelSwitch extends IOTCommand {//{{{
        public ChannelSwitch(String key) {
            super(key);
            iotFollowCommand(key);
        }

        public int call(String params) {
            Log.i(TAG, "iot---> " + name() + "( " + params + ")");

            { // for debug
                updatePropertyToUI(Constants.IOT_CMD_VOLUME_SWITCH, params);
            }
            return 0;
        }
    }//}}}

    public class AppStart extends IOTCommand {//{{{
        public AppStart(String key) {
            super(key);
            iotFollowCommand(key);
        }

        public int call(String params) {
            return 0;
        }
    }//}}}

    public class VideoSearch extends IOTCommand {//{{{
        public VideoSearch(String key) {
            super(key);
            iotFollowCommand(key);
        }

        public int call(String params) {
            return 0;
        }
    }//}}}

    public class TextPush extends IOTCommand {//{{{
        public TextPush(String key) {
            super(key);
            iotFollowCommand(key);
        }

        public int call(String params) {
            return 0;
        }
    }//}}}

    public class VideoPlay extends IOTCommand {//{{{
        public VideoPlay(String key) {
            super(key);
            iotFollowCommand(key);
        }

        public int call(String params) {
            return 0;
        }
    }//}}}

    public void iotCommandCallback(String cmd, String data) {//{{{
        Log.d(TAG, " iotCommandCallback(" + data + ")");
        IOTCommand iotCmd = mCommands.get(cmd);
        if (iotCmd == null)
            return;
        try {
            JSONObject jsonObject = new JSONObject(data);
            JSONObject params = jsonObject.getJSONObject("parameters"); 
            if (params != null)
                iotCmd.call(params.toString());
        } catch (JSONException e) {
            Log.e(TAG, "Json parse error: " + e);
        }
    }//}}}

    public String iotPropertyGet(String key) {//{{{
        IOTProperty iotPro = mProperties.get(key);
        if (iotPro != null)
            return iotPro.get();
        return "";
    }//}}}

    public void iotPropertySet(String key, String val) {//{{{
        IOTProperty iotPro = mProperties.get(key);
        if (iotPro != null)
            iotPro.set(val);
    }//}}}

    /* Simulate UI update data, maybe delete */
    public void updatePropertyFromUI(String key, String val, boolean urgent) {//{{{
        IOTProperty iotPro = mProperties.get(key);
        if (iotPro != null) {
            iotPro.update(val);
            if (urgent)
                iotReportProperty(key, val);
        }
    }//}}}

    /* Simulate UI update data, maybe delete */
    public void updatePropertyToUI(String action, String val) {//{{{
        Intent intent = new Intent(action);
        intent.putExtra("value", val);
        mContext.sendBroadcast(intent);
    }//}}}
}
