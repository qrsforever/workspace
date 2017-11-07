package com.java.learn;

import java.io.IOException;
import java.net.InetSocketAddress;
import java.nio.ByteBuffer;
import java.nio.channels.SelectionKey;
import java.nio.channels.Selector;
import java.nio.channels.SocketChannel;
import java.util.Iterator;

public class NioClient
{
    private Selector selector = null;

    public NioClient() {
    }

    public NioClient init(String ip, int port) throws IOException {
        selector = Selector.open();

        SocketChannel channel = SocketChannel.open();
        channel.configureBlocking(false);

        // 客户端连接服务器，需要调用channel.finishConnect();才能实际完成连接
        channel.connect(new InetSocketAddress(ip, port));
        channel.register(selector, SelectionKey.OP_CONNECT);
        return this;
    }

    public void listen() throws IOException {
        System.out.println("Client start success!");
        
        while(true) {
            int num = selector.select();     
            if (num <= 0)
                continue;

            SocketChannel channel = null;

            Iterator<SelectionKey> itkeys = selector.selectedKeys().iterator();
            while(itkeys.hasNext()) {
                SelectionKey key = itkeys.next();
                if (key.isConnectable()) {
                    channel = (SocketChannel)key.channel(); 
                    // 在等待一下, 使其真正连接上
                    if (channel.isConnectionPending())  {
                        channel.finishConnect();
                    }
                    channel.write(ByteBuffer.wrap(new String("Hi, Server").getBytes()));
                    channel.configureBlocking(false);   
                    channel.register(selector, SelectionKey.OP_READ);
                } else if (key.isReadable()) {
                    channel = (SocketChannel)key.channel();
                    ByteBuffer buffer = ByteBuffer.allocate(1024);
                    channel.read(buffer);
                    byte[] data = buffer.array();
                    String msg  = new String(data);
                    System.out.println("From Server: " + msg);
                }
                itkeys.remove();
            }
        }
        // selector.close();
    }

    public static void main( String[] args ) throws IOException {
        new NioClient().init("127.0.0.1", 9798).listen();
    }
}
