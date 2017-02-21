package com.hybroad.client;

import android.os.IBinder;
import android.os.ServiceManager;

import com.hybroad.aidl.IQAudioService;

public class QAudioManager {
    final static private String AUDIO_SERVICE_NAME = "Qaudio_service";
    private static IQAudioService sAudioservice = null;
    private QAudioManager() {
    }

    static IQAudioService getService() {
        if (sAudioservice  == null) {
            IBinder binder = ServiceManager.getService(AUDIO_SERVICE_NAME);
            sAudioservice = IQAudioService.Stub.asInterface(binder);
        }
        return sAudioservice;
    }
}
