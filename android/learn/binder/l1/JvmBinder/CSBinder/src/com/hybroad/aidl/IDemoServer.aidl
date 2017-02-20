package com.hybroad.aidl;
import com.hybroad.aidl.OperandData;
import com.hybroad.aidl.ICallback;

interface IDemoServer {
    int calculate(in OperandData o, ICallback cb);
}

