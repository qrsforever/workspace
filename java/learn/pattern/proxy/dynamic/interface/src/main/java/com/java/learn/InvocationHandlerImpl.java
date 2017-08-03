package com.java.learn;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import org.apache.log4j.Logger;

public class InvocationHandlerImpl implements InvocationHandler {
    private LeecoTV realObjTV;
    private static final Logger log = Logger.getLogger(InvocationHandlerImpl.class);

    public InvocationHandlerImpl(LeecoTV tv) {
        this.realObjTV = tv;
    }

    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        log.info("invoke method:" + method.getName() + " before");
        method.invoke(realObjTV, args);
        log.info("invoke method:" + method.getName() + " after");
        return null;
    }
}
