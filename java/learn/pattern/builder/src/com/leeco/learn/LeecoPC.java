package com.leeco.learn;

import java.util.ArrayList;
import java.util.List;

public class LeecoPC {

    private List<IPCAccessory> _mAccessories = new ArrayList<IPCAccessory>();

    public LeecoPC() {

    }

    public void addAccessory(IPCAccessory acc) {
        _mAccessories.add(acc);
    }

    public float getPrices() {
        float sum = 0.0f;
        for (IPCAccessory acc : _mAccessories) {
            sum += acc.price();
        }
        return sum;
    }

    public void showDetails() {
        for (IPCAccessory acc : _mAccessories) {
            System.out.println("Name: " + acc.name() + "  Price: " + acc.price());
        }
    }

    /* method 2 */
    public static Builder builder() {
        return new Builder();
    }

    public static final class Builder {
        public LeecoPC build() {
            LeecoPC pc = new LeecoPC();
            pc.addAccessory(new CpuAccessory());
            pc.addAccessory(new MemAccessory());
            pc.addAccessory(new DiskAccessory());
            return pc;
        }
    } 
}
