package com.leeco.learn;

public class LeecoBuilder {

    public LeecoBuilder() {
        
    }

    public LeecoPC build() {
        LeecoPC pc = new LeecoPC();
        pc.addAccessory(new CpuAccessory());
        pc.addAccessory(new MemAccessory());
        pc.addAccessory(new DiskAccessory());
        return pc;
    }
}
