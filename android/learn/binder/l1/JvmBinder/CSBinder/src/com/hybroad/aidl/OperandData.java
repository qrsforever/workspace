package com.hybroad.aidl;

import android.os.Parcel;
import android.os.Parcelable;

public class OperandData implements Parcelable
{
    public int data1;
    public int data2;
    public String operator;

    public OperandData() {
        data1 = 1;
        operator = "+";
        data2 = 2;
    }

    public OperandData(int d1, String oper, int d2) {
        data1 = d1;
        data2 = d2;
        operator = oper;
    }

    public OperandData(Parcel in) {
        data1 = in.readInt();
        operator = in.readString();
        data2 = in.readInt();
    }

    @Override
    public int describeContents() {
        return 0;
    }

    @Override
    public void writeToParcel(Parcel dest, int flags) {
        // correspond to 'createFromParcel'
        dest.writeInt(data1);
        dest.writeString(operator);
        dest.writeInt(data2);
    }

    public static final Parcelable.Creator<OperandData> CREATOR = new Creator<OperandData>() {
        @Override
        public OperandData createFromParcel(Parcel source) {
            return new OperandData(source);
        }

        @Override
        public OperandData[] newArray(int size) {
            return new OperandData[size];
        }
    };
}
