package edu.logic.server;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import edu.logic.constant.Constant;
/**
 * Server��
 * @author Logic Luo
 */
public class Server extends Thread {
    private Socket socket = null;
    private ServerSocket serverSocket = null;
    public static int count = 0;

    /**
     * �޲ι��캯��
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
            System.out.println("����socket������");
            try {
                // �����������socket
                socket = serverSocket.accept();
                System.out.println(count++);
                // �����߳�, ���̸߳���ر�socket
                new ServerThread(socket).start();
            } catch (IOException e) {
                e.printStackTrace();
            } 
        }
    }

    /**
     * ������ 
     * @param args
     */
    public static void main(String[] args) {
        // ����ǰ̨�߳̽���jvm���˳���
        new Server().start();
    }
}
