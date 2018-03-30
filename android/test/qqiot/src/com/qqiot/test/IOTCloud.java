package com.qqiot.test;

import android.content.Context;
import android.util.Log;
import android.content.Intent;

import java.util.HashMap;
import java.util.Map;

import com.qcloud.restapi.iotcore.api.TXIotCloud;
import com.qcloud.restapi.iotcore.request.*;
import com.qcloud.restapi.iotcore.response.*;
import com.qcloud.restapi.iotcore.utils.HttpClient;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;

public class IOTCloud {
    public static final String TAG = IOTCloud.class.getSimpleName();
    private Context  mContext;

    private Map<String, IOTProperty> mProperties = null;
    private Map<String, IOTCommand> mCommands = null;

    private static IOTCloud mIotProxy = null;
    private TXIotCloud mIotCloud = null;
    private static final String mProductID = "38GBCH2FO2";
    private static final String mDeviceName = "testshadow";

    private static final String SECRET_ID =  "AKIDc9kEZPA20ugHl9R2c2Pgqtsiw5AGq74Y";
    private static final String SECRET_KEY = "Z3Y8qVzJWrAnLn9OT2Uq1Md1XGsIMJ5f";

    public IOTCloud(Context context) {//{{{
        mContext = context;
        mProperties = new HashMap<String, IOTProperty>();
        mCommands = new HashMap<String, IOTCommand>();
        System.getProperties().setProperty("https.proxyHost", "dev-proxy.oa.com");
        System.getProperties().setProperty("https.proxyPort", "8080");
        iotSetup();
        new Thread(new Runnable() {
            @Override
            public void run() {
                mIotCloud = new TXIotCloud(SECRET_ID, SECRET_KEY);

                // String ret = HttpClient.httpsRequest(null, HttpClient.METHOD_GET, null, 30*1000, 30*1000);
                // System.out.println("### iot response = " + ret);
                try {
                    CloseableHttpClient client = HttpClients.createDefault();

                    String targetUrl = "https://iotcloud.api.qcloud.com/v2/index.php?Action=GetDeviceShadow&Nonce=363650530&Region=gz&SecretId=AKIDc9kEZPA20ugHl9R2c2Pgqtsiw5AGq74Y&Timestamp=1522305679&deviceName=testshadow&productID=38GBCH2FO2&Signature=GKqthTzj31xq2PUpXKJSU%2Bo0DsM%3D";
                    HttpGet get = new HttpGet(targetUrl);

                    CloseableHttpResponse res = client.execute(get);
                    System.out.println("### + iot status = " + res.getStatusLine().getStatusCode());
                    HttpEntity entity = res.getEntity();
                    String html = EntityUtils.toString(entity);
                    System.out.println(html);
                    client.close();

                    Thread.sleep(30000);
                } catch (Exception e){
                    e.printStackTrace();
                    System.out.println("### iot error = " + e);
                }
            }
        }).start();
    }//}}}

    public static IOTCloud getInstance(Context context) {//{{{
        if (mIotProxy  == null) {
            mIotProxy  = new IOTCloud(context);
        }
        return mIotProxy;
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

    public int testService() {
        /*
        Log.i(TAG,  " iot testService ");
        GetDeviceShadowResponse response = mIotCloud.getDeviceShadow(new GetDeviceShadowRequest(mProductID, mDeviceName));
        String data = response.getData();
        Log.i(TAG, "iot data:" + data);
        String payload = response.getPayload();
        Log.i(TAG, "iot payload:" + payload);
        String version = response.getPayloadVersion();
        Log.i(TAG, "iot version:" + version);
        Log.i(TAG, "iot response:" + response);
        */
        return 0;
    }

    abstract public class IOTProperty {//{{{
        String mKey;
        String mVal;
        protected IOTProperty(String key) {
            mKey = key;
        }
        public String key() { return mKey; }
        protected abstract String get();
        protected abstract int set(String val);
        protected void update(String val) {
            String json = "{\"desired\": {\"" + key() + "\":" + Integer.parseInt(val) +"}}";
            UpdateDeviceShadowResponse response = mIotCloud.updateDeviceShadow(
                    new UpdateDeviceShadowRequest(mProductID, mDeviceName, json, 0));
            Log.i(TAG, "response:" + response);
        }
    }//}}}

    abstract public class IOTCommand {//{{{
        String mName;
        protected IOTCommand(String name) {
            mName = name;
        }
        public String name() { return mName; }
        protected abstract int call(String params);
    }//}}}

    public class Power extends IOTProperty {//{{{
        public Power(String key) {
            super(key);
        }

        public String get() {
            Log.i(TAG, "iot---> get(" + key() + ")");
            return "";
        }

        public int set(String val) {
            Log.i(TAG, "iot---> set(" + key() + ", " + val + ")");
            return 0;
        }

        public void update(String val) {
            Log.i(TAG, "iot---> update(" + key() + ", " + val + ")");
            super.update(val);
        }
    }//}}}

    public class Signal extends IOTProperty {//{{{
        public Signal(String key) {
            super(key);
        }

        public String get() {
            Log.i(TAG, "iot---> get(" + key() + ")");
            return "0";
        }

        public int set(String val) {
            Log.i(TAG, "iot---> set(" + key() + ", " + val + ")");
            return 0;
        }

        public void update(String val) {
            Log.i(TAG, "iot---> update(" + key() + ", " + val + ")");
            super.update(val);
        }
    }//}}}

    public class Brightness extends IOTProperty {//{{{
        public Brightness(String key) {
            super(key);
        }

        public String get() {
            Log.i(TAG, "iot---> get(" + key() + ")");
            return "";
        }

        public int set(String val) {
            Log.i(TAG, "iot---> set(" + key() + ", " + val + ")");
            return 0;
        }

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
            Log.i(TAG, "iot---> " + name() + "( " + params + ")");

            return 0;
        }
    }//}}}

    public class ChannelSwitch extends IOTCommand {//{{{
        public ChannelSwitch(String key) {
            super(key);
        }

        public int call(String params) {
            Log.i(TAG, "iot---> " + name() + "( " + params + ")");

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
        IOTProperty iotPro = mProperties.get(name);
        if (iotPro == null)
            return ;
        iotPro.update(value);
    }//}}}
}
