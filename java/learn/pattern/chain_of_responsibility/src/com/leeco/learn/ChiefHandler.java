package com.leeco.learn;

public class ChiefHandler extends Handler {

    @Override
    public boolean handlerMessage(int what) {
        if (what > eLevel_Chief) {
            Handler h = getSuccessor();
            if (h != null)
                return h.handlerMessage(what);
            return false;
        }
        System.out.println("Chief just do it!");
        return true;
    }
    
}
