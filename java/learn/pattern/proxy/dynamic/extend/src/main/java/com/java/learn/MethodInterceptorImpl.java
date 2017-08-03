package com.java.learn;

import java.lang.reflect.Method;

import org.apache.log4j.Logger;
import net.sf.cglib.proxy.MethodInterceptor;
import net.sf.cglib.proxy.MethodProxy;

public class MethodInterceptorImpl implements MethodInterceptor {
    public static final Logger log = Logger.getLogger(MethodInterceptorImpl.class);

    @Override
    public Object intercept(Object obj, Method method, Object[] args, MethodProxy proxy) throws Throwable {
        log.info("invoke method:" + method.getName() + " before");
        proxy.invokeSuper(obj, args);
        log.info("invoke method:" + method.getName() + " after");
        return null;
    }
}
