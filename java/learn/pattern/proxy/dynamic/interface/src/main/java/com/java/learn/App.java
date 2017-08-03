package com.java.learn;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Proxy;

public class App {
    public static void main(String[] args) {
        System.out.println(System.getProperty("java.class.path"));

        LeecoTV tv = new LeecoTV();
        // 1
        ClassLoader cl = tv.getClass().getClassLoader();
        // 2
        Class<?>[] ifaces = tv.getClass().getInterfaces();
        // 3 
        InvocationHandler handle = new InvocationHandlerImpl(tv);
        // 4
        Object proxy = Proxy.newProxyInstance(cl, ifaces, handle);
        // 5
        ((INetwork)proxy).connect();
        ((IScreen)proxy).display();
                          
        // 将生成的字节码输出到文件中
        ProxyUtils.generateClassFile(tv.getClass(), "LeecoTVProxy");  
    }                     
}                         
                          
/*                        
 *                        
 *                    +---------------------------------------------------------------------+
 *                    |                                                                     |
 *             +------v----+         +-----------+                                          |
 *             |           |         |           |                                          |
 *             | INetwork  |         |  IScreen  |<-------------------------------------+   |
 *             |           |         |           |                                      |   |
 *             +-----^-----+         +-----^-----+                                      |   |
 *                   |                     |                                            |   |
 *                   +------+    +---------+                                            |   |
 *                          |    |                                                      |   |
 *                       +--+----+---+                                                  |   |
 *                       |           |                     +------------------------+   |   |
 *                       |  LeecoTV  |<--------------------+                        |   |   |
 *                       |           |                     | InvocationHandlerImpl  |   |   |
 *                       +-----------+                     |                        |   |   |
 *                                                         +------------^-----------+   |   |
 *                                                                      |               |   |
 *                                                                      |               |   |
 *                                                                      |               |   |
 *                                                                      |               |   |
 *                                           extend            +-------------------+    |   |
 *                                              +--------------|                   |    |   |
 *                                              |              |   LeecoTVProxy    | ---+   |
 *                                      +-------V----+         |                   | -------+
 *                                      |            |         +-------------------+  implement
 *                                      |    Proxy   |                               
 *                                      |            |                               
 *                                      +------------+                               
 * */                                                                                  
