package com.qqiot.test;

import android.content.Context;
import android.util.Log;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.os.Message;

import java.util.HashMap;
import java.util.Map;

import android.os.HandlerThread;

import com.qcloud.restapi.iotcore.api.TXIotCloud;
import com.qcloud.restapi.iotcore.request.*;
import com.qcloud.restapi.iotcore.response.*;

public class IOTCloud {
    public static final String TAG = IOTCloud.class.getSimpleName();

    private static final int UPDATE_PROPERTY = 1;
    private static final int SEND_COMMAND = 2;

    private Map<String, IOTProperty> mProperties = null;
    private Map<String, IOTCommand> mCommands = null;

    private HandlerThread mIotThread;
    private Handler mIotHandler;

    private static IOTCloud mIotProxy = null;
    private TXIotCloud mIotCloud = null;
    private static final String mProductID = "38GBCH2FO2";
    private static final String mDeviceName = "testshadow";

    private static final String SECRET_ID =  "AKIDc9kEZPA20ugHl9R2c2Pgqtsiw5AGq74Y";
    private static final String SECRET_KEY = "Z3Y8qVzJWrAnLn9OT2Uq1Md1XGsIMJ5f";

    public IOTCloud() {//{{{
        mProperties = new HashMap<String, IOTProperty>();
        mCommands = new HashMap<String, IOTCommand>();
        mIotCloud = new TXIotCloud(SECRET_ID, SECRET_KEY);
        mIotThread = new HandlerThread("iot");
        mIotThread.start();
        mIotHandler = new IOTHandler(mIotThread.getLooper());
        iotSetup();
    }//}}}

    public static IOTCloud getInstance() {//{{{
        if (mIotProxy  == null) {
            mIotProxy  = new IOTCloud();
        }
        return mIotProxy;
    }//}}}

    class IOTHandler extends Handler {//{{{
        public IOTHandler(Looper looper) {
            super(looper);

        }

        @Override
        public void handleMessage(Message msg) {
            switch (msg.what) {
                case UPDATE_PROPERTY:
                    mIotCloud.updateDeviceShadow(
                            new UpdateDeviceShadowRequest(
                                mProductID,
                                mDeviceName,
                                msg.getData().getString("payload"), 0)
                            );
                    return;

                case SEND_COMMAND:
                    mIotCloud.publish(
                            new PublishRequest(
                                mProductID, 
                                mDeviceName, 
                                mProductID +"/" + mDeviceName + "/control",
                                msg.getData().getString("payload"))
                            );
                    return;
            }
            super.handleMessage(msg);
        }
    }//}}}

    public int iotSetup() {//{{{
        mProperties.put(Constants.IOT_PRO_POWER, new Power(Constants.IOT_PRO_POWER));
        mProperties.put(Constants.IOT_PRO_SIGNAL, new Signal(Constants.IOT_PRO_SIGNAL));
        mProperties.put(Constants.IOT_PRO_BRIGHTNESS, new Brightness(Constants.IOT_PRO_BRIGHTNESS));

        mCommands.put(Constants.IOT_CMD_VOLUME_SWITCH, new VolumeSwitch(Constants.IOT_CMD_VOLUME_SWITCH));
        mCommands.put(Constants.IOT_CMD_CHANNEL_SWITCH, new ChannelSwitch(Constants.IOT_CMD_CHANNEL_SWITCH));
        mCommands.put(Constants.IOT_CMD_APP_START, new AppStart(Constants.IOT_CMD_APP_START));
        mCommands.put(Constants.IOT_CMD_VIDEO_SEARCH, new VideoSearch(Constants.IOT_CMD_VIDEO_SEARCH));
        mCommands.put(Constants.IOT_CMD_TEXT_PUSH, new TextPush(Constants.IOT_CMD_TEXT_PUSH));
        mCommands.put(Constants.IOT_CMD_VIDEO_PLAY, new VideoPlay(Constants.IOT_CMD_VIDEO_PLAY));
        return 0;
    }//}}}

    public int testService() {//{{{
        Log.i(TAG,  " iot testService ");
        GetDeviceShadowResponse response = mIotCloud.getDeviceShadow(new GetDeviceShadowRequest(mProductID, mDeviceName));
        String data = response.getData();
        Log.i(TAG, "iot data:" + data);
        String payload = response.getPayload();
        Log.i(TAG, "iot payload:" + payload);
        String version = response.getPayloadVersion();
        Log.i(TAG, "iot version:" + version);
        Log.i(TAG, "iot response:" + response);
        return 0;
    }//}}}

    abstract public class IOTProperty {//{{{
        String mKey;
        String mVal;
        protected IOTProperty(String key) {
            mKey = key;
        }
        public String key() { return mKey; }
        // protected abstract String get();
        // protected abstract int set(String val);
        protected void update(String val) {
            String json = "{\"desired\": {\"" + key() + "\":" + Integer.parseInt(val) +"}}";
            Bundle bundle = new Bundle();
            bundle.putString("payload", json);

            Message msg = mIotHandler.obtainMessage();
            msg.what = UPDATE_PROPERTY;
            msg.setData(bundle);
            mIotHandler.sendMessage(msg);
        }
    }//}}}

    abstract public class IOTCommand {//{{{
        String mCmd;
        protected IOTCommand(String cmd) {
            mCmd = cmd;
        }
        public String cmd() { return mCmd; }
        protected int call(String params) {
            String json = "{\"command\": \"" + cmd() + "\", \"parameters\":{" + params + "}, \"targetDevice\":\"" + mDeviceName + "\"}";
            Bundle bundle = new Bundle();
            bundle.putString("payload", json);

            Message msg = mIotHandler.obtainMessage();
            msg.what = SEND_COMMAND;
            msg.setData(bundle);
            mIotHandler.sendMessage(msg);
            return 0;
        }
    }//}}}

    public class Power extends IOTProperty {//{{{
        public Power(String key) {
            super(key);
        }
        
/*            public String get() {
 *                Log.i(TAG, "iot---> get(" + key() + ")");
 *                return "";
 *            }
 * 
 *            public int set(String val) {
 *                Log.i(TAG, "iot---> set(" + key() + ", " + val + ")");
 *                return 0;
 *            } */
          
        public void update(String val) {
            Log.i(TAG, "iot---> update(" + key() + ", " + val + ")");
            super.update(val);
        }
    }//}}}

    public class Signal extends IOTProperty {//{{{
        public Signal(String key) {
            super(key);
        }

/*         public String get() {
 *             Log.i(TAG, "iot---> get(" + key() + ")");
 *             return "0";
 *         }
 * 
 *         public int set(String val) {
 *             Log.i(TAG, "iot---> set(" + key() + ", " + val + ")");
 *             return 0;
 *         } */

        public void update(String val) {
            Log.i(TAG, "iot---> update(" + key() + ", " + val + ")");
            super.update(val);
        }
    }//}}}

    public class Brightness extends IOTProperty {//{{{
        public Brightness(String key) {
            super(key);
        }

/*         public String get() {
 *             Log.i(TAG, "iot---> get(" + key() + ")");
 *             return "";
 *         }
 * 
 *         public int set(String val) {
 *             Log.i(TAG, "iot---> set(" + key() + ", " + val + ")");
 *             return 0;
 *         } */

        public void update(String val) {
            Log.i(TAG, "iot---> update(" + key() + ", " + val + ")");
            super.update(val);
        }
    }//}}}

    public class VolumeSwitch extends IOTCommand {//{{{
        public VolumeSwitch(String key) {
            super(key);
        }

        public int call(String params) {
            Log.i(TAG, "iot---> " + cmd() + "( " + params + ")");
            return super.call(params);
        }
    }//}}}

    public class ChannelSwitch extends IOTCommand {//{{{
        public ChannelSwitch(String key) {
            super(key);
        }

        public int call(String params) {
            Log.i(TAG, "iot---> " + cmd() + "( " + params + ")");

            return 0;
        }
    }//}}}

    public class AppStart extends IOTCommand {//{{{
        public AppStart(String key) {
            super(key);
        }

        public int call(String params) {
            return 0;
        }
    }//}}}

    public class VideoSearch extends IOTCommand {//{{{
        public VideoSearch(String key) {
            super(key);
        }

        public int call(String params) {
            return 0;
        }
    }//}}}

    public class TextPush extends IOTCommand {//{{{
        public TextPush(String key) {
            super(key);
        }

        public int call(String params) {
            return 0;
        }
    }//}}}

    public class VideoPlay extends IOTCommand {//{{{
        public VideoPlay(String key) {
            super(key);
        }

        public int call(String params) {
            return 0;
        }
    }//}}}

    public void updateDeviceShadow(String name, String value) {//{{{
        Log.i(TAG, " updateDeviceShadow(" + name + ", " + value + ")");
        final IOTProperty iotPro = mProperties.get(name);
        if (iotPro == null)
            return ;
        iotPro.update(value);
    }//}}}

    public void contrlDeviceShadow(String cmd, String value) {//{{{
        Log.i(TAG, " contrlDeviceShadow(" + cmd + ")");
        final IOTCommand iotCmd = mCommands.get(cmd);
        if (iotCmd == null)
            return ;
        iotCmd.call(value);
    }//}}}
}
