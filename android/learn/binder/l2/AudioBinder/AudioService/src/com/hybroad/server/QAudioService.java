package com.hybroad.server;

import android.os.RemoteException;
import com.hybroad.aidl.IQAudioService ;

public class QAudioService extends IQAudioService.Stub {
    private int volume;
    @Override
    public void setVolume(int val) throws RemoteException {
        this.volume = val;
    }

    @Override
    public int getVolume() throws RemoteException {
        return this.volume;
    }
}
