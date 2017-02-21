package com.hybroad.server;

import android.app.Application;
import android.os.ServiceManager;

public class QAudioServiceApplication extends Application {
    final private String AUDIO_SERVICE_NAME = "Qaudio_service";
    @Override
    public void onCreate() {
        super.onCreate();
        ServiceManager.addService(AUDIO_SERVICE_NAME, new QAudioService());
    } 
}
