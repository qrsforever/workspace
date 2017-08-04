package com.java.learn;

import java.io.FileOutputStream;
import java.io.IOException;
import sun.misc.ProxyGenerator;

public class ProxyUtils {

    /**
     * 将class字节码保持到硬盘中
     *
     * @param clazz 需要生成proxy类的类
     * @param proxyName 代理类的名字
     */
    public static void generateClassFile(Class<?> clazz, String proxyName) {
        byte[] classFile = ProxyGenerator.generateProxyClass(proxyName, clazz.getInterfaces());
        String paths = clazz.getResource(".").getPath();

        System.out.println(paths);
        FileOutputStream out = null;

        try {
            //保留到硬盘中
            out = new FileOutputStream(paths + proxyName + ".class");
            out.write(classFile);
            out.flush();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try {
                out.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
