package com.leeco.learn;

public class EmployeeHandler extends Handler {

    @Override
    public boolean handlerMessage(int what) {
        if (what > eLevel_Employee) {
            Handler h = getSuccessor();
            if (h != null)
                return h.handlerMessage(what);
            return false;
        }
        System.out.println("Employee can do it!");
        return true;
    }
    
}
