package com.java.learn;

import java.io.FileOutputStream;
import java.io.IOException;
import net.sf.cglib.proxy.Enhancer;
import net.sf.cglib.core.DebuggingClassWriter;

public class App {
    public static void main(String[] args) {
        LeecoTV tv = new LeecoTV();
        Enhancer enhancer = new Enhancer();
        enhancer.setSuperclass(tv.getClass());
        enhancer.setCallback(new MethodInterceptorImpl());
        LeecoTV proxy =(LeecoTV)enhancer.create();
        proxy.connect();
        proxy.display();
        
        // Debug
    /*     FileOutputStream out = null;
     *     try {
     *         DebuggingClassWriter cw = new DebuggingClassWriter(0);
     *         enhancer.generateClass(cw);
     *         out = new FileOutputStream("LeecoTVProxy.class");
     *         out.write(cw.toByteArray());
     *         out.flush();
     *     } catch (Exception e) {
     *         e.printStackTrace();
     *     } finally {
     *         try {
     *             out.close();
     *         } catch (IOException e) {
     *             e.printStackTrace();
     *         }
     *     }
     * */
    }
}
