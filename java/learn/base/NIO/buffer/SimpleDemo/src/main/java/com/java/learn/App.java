package com.java.learn;

import java.nio.ByteBuffer;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args ) {
        System.out.println("----------Test allocate--------");  

        System.out.println("before alocate:" + Runtime.getRuntime().freeMemory());  
        // JDK1.8: 10240000
        ByteBuffer buffer = ByteBuffer.allocate(10240000);  
        System.out.println("buffer = " + buffer);  
        System.out.println("after alocate:" + Runtime.getRuntime().freeMemory());  

        // 这部分直接用的系统内存，所以对JVM的内存没有影响  
        ByteBuffer directBuffer = ByteBuffer.allocateDirect(102400);  
        System.out.println("directBuffer = " + directBuffer);  
        System.out.println("after direct alocate:" + Runtime.getRuntime().freeMemory());  

        System.out.println("----------Test wrap--------");  
        byte[] bytes = new byte[32];  
        buffer = ByteBuffer.wrap(bytes);  
        System.out.println(buffer);  
        // 偏移量和长度
        buffer = ByteBuffer.wrap(bytes, 10, 10);  
        System.out.println(buffer);   

        System.out.println("--------Test reset----------");  
        // 初始化: position = 0;limit = capacity;mark = -1, 不影响底层byte数组的内容
        buffer.clear();  
        buffer.position(5);  
        // 记录当前的position
        buffer.mark();  
        buffer.position(10);  
        System.out.println("before reset:" + buffer);  
        // 恢复到之前记录的position
        buffer.reset();  
        System.out.println("after reset:" + buffer);  

        System.out.println("--------Test rewind--------");  
        buffer.clear();  
        buffer.position(10);  
        buffer.limit(15);  
        System.out.println("before rewind:" + buffer);  
        // 不改变limit值, 设置mark=-1, position = 0
        buffer.rewind();  
        System.out.println("before rewind:" + buffer);  

        System.out.println("--------Test compact--------");  
        buffer.clear();  
        // 写入
        buffer.put("abcd".getBytes());  
        System.out.println("before compact:" + buffer);  
        System.out.println(new String(buffer.array()));  
        // 写转读 (position = 0, limit = 4 ("abcd")
        buffer.flip();  
        System.out.println("after flip:" + buffer);  
        System.out.println((char) buffer.get());  
        System.out.println((char) buffer.get());  
        System.out.println((char) buffer.get());  
        System.out.println("after three gets:" + buffer);  
        // 仍然输出"abcd"
        System.out.println(new String(buffer.array()));  
        // 把剩下的内容从0位子copy
        buffer.compact();  
        System.out.println("after compact:" + buffer);  
        System.out.println(new String(buffer.array()));

        System.out.println("------Test get-------------");  
        buffer = ByteBuffer.allocate(32);  
        buffer.put((byte) 'a').put((byte) 'b').put((byte) 'c').put((byte) 'd')  
            .put((byte) 'e').put((byte) 'f');  
        System.out.println("before flip()" + buffer);  
        // 转换为读取模式  
        buffer.flip();  
        System.out.println("before get():" + buffer);  
        System.out.println((char) buffer.get());  
        System.out.println("after get():" + buffer);  
        // get(index)不影响position的值  
        System.out.println((char) buffer.get(2));  
        System.out.println("after get(index):" + buffer);  
        byte[] dst = new byte[10];  
        // 从position位置读取2个字节, 0不是从开头位置
        buffer.get(dst, 0, 2);  
        System.out.println("after get(dst, 0, 2):" + buffer);  
        System.out.println("dst:" + new String(dst));  
        System.out.println("buffer now is:" + buffer);  
        System.out.println(new String(buffer.array()));  

        System.out.println("--------Test put-------");  
        ByteBuffer bb = ByteBuffer.allocate(32);  
        System.out.println("before put(byte):" + bb);  
        System.out.println("after put(byte):" + bb.put((byte) 'z'));  
        // put(2,(byte) 'c')不改变position的位置  
        System.out.println(bb.put(2, (byte) 'c'));  
        System.out.println("after put(2,(byte) 'c'):" + bb);  
        System.out.println(new String(bb.array()));  
        // 这里的buffer是 abcdef[pos=3 lim=6 cap=32]  
        bb.put(buffer);  
        System.out.println("after put(buffer):" + bb);  
        System.out.println(new String(bb.array())); 
    }
}
