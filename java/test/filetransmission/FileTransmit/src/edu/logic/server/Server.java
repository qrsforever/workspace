package edu.logic.server;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import edu.logic.constant.Constant;
/**
 * Server类
 * @author Logic Luo
 */
public class Server extends Thread {
    private Socket socket = null;
    private ServerSocket serverSocket = null;
    public static int count = 0;

    /**
     * 无参构造函数
     */
    public Server(){
        try {
            serverSocket = new ServerSocket(Constant.PORT);
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }

    @Override
    public void run() {
        while(true) {
            System.out.println("进行socket监听！");
            try {
                // 获监听过来的socket
                socket = serverSocket.accept();
                System.out.println(count++);
                // 服务线程, 该线程负责关闭socket
                new ServerThread(socket).start();
            } catch (IOException e) {
                e.printStackTrace();
            } 
        }
    }

    /**
     * 主函数 
     * @param args
     */
    public static void main(String[] args) {
        // 所有前台线程结束jvm才退出。
        new Server().start();
    }
}
