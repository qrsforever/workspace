package com.leeco.learn;

public class DiskAccessory implements IPCAccessory {

    @Override
    public float price() {
        return 50.5f;
    }

    @Override
    public String name() {
        return "Disk";
    }

}
