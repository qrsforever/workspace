package com.leeco.learn;

public class CpuAccessory implements IPCAccessory {

    @Override
    public float price() {
        return 100.0f;
    }

    @Override
    public String name() {
        return "CPU";
    }

}
