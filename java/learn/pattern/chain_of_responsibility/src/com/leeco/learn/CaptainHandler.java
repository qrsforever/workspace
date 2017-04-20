package com.leeco.learn;

public class CaptainHandler extends Handler {

    @Override
    public boolean handlerMessage(int what) {
        System.out.println("Captain do something before successor!");
        if (what > eLevel_Captain) {
            Handler h = getSuccessor();
            if (h != null)
                return h.handlerMessage(what);
            return false;
        }
        System.out.println("Captain just do it!");
        return true;
    }
    
}
