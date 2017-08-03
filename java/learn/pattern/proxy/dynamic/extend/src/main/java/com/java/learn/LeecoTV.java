package com.java.learn;

import org.apache.log4j.Logger;

public class LeecoTV implements IScreen, INetwork {
    public static final Logger log = Logger.getLogger(LeecoTV.class);

    public void display() {
        log.info("display");
    }

    public void connect() {
        log.info("connect");
    }
}
