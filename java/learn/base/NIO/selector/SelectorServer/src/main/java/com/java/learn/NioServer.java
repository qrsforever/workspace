package com.java.learn;

import java.io.IOException;
import java.net.InetSocketAddress;
import java.net.ServerSocket;
import java.nio.ByteBuffer;
import java.nio.channels.SelectionKey;
import java.nio.channels.Selector;
import java.nio.channels.ServerSocketChannel;
import java.nio.channels.SocketChannel;
import java.util.Iterator;
import java.util.Random;

public class NioServer
{
    // 通道管理器
    private Selector selector;
    private Random random = new Random();

    public NioServer() {
    }

    public NioServer init(int port)  throws IOException {
        ServerSocketChannel serverSocketChannel = ServerSocketChannel.open();
        ServerSocket socket = serverSocketChannel.socket();
        socket.bind(new InetSocketAddress(port));

        serverSocketChannel.configureBlocking(false);

        // 获取通道管理器, 并注册Accept事件
        selector = Selector.open();
        serverSocketChannel.register(selector, SelectionKey.OP_ACCEPT);
        return this;
    }

    public void listen() throws IOException {
        System.out.println("Server start success!");
        Iterator<SelectionKey> itkeys = null;
        while(true) {
            int num = selector.select();
            if (num <= 0)
                continue;
            SocketChannel channel = null;
            itkeys = selector.selectedKeys().iterator();
            while(itkeys.hasNext()) {
                SelectionKey key = itkeys.next();
                // 删除该key防止重复
                if (key.isAcceptable()) {
                    ServerSocketChannel ss = (ServerSocketChannel)key.channel();
                    // 获取Client端的连接通道
                    channel = ss.accept();
                    // 向client发送消息
                    channel.write(ByteBuffer.wrap(new String("I am Server, Hi!").getBytes())); 
                    // 为client通道注册Read事件, 并attach一个随机数client-id
                    channel.configureBlocking(false);
                    channel.register(selector, SelectionKey.OP_READ, "Client-" + Integer.toString(random.nextInt(10)));
                } else if (key.isReadable()) {
                    channel = (SocketChannel)key.channel();
                    try {
                        ByteBuffer buffer = ByteBuffer.allocate(1024);
                        int read = channel.read(buffer);
                        if (read > 0) {
                            String clientId = key.attachment().toString();
                            // String msg  = buffer.toString(); // 这个结果应该不是你想要的
                            byte[] data = buffer.array();
                            String msg  = new String(data);
                            System.out.println("From " + clientId + ":" + msg);
                        }
                    } catch (IOException e) {
                        // Client通道关闭了
                        key.cancel(); 
                        channel.socket().close();
                        channel.close();
                    }
                }
                itkeys.remove();
            }
        }
        // selector.close();
    }

    public static void main( String[] args ) throws IOException {
        new NioServer().init(9798).listen();
    }
}
