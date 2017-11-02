package edu.logic.server;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.net.Socket;

import edu.logic.common.Transmission;
import edu.logic.constant.Constant;

/**
 * 处理文件的上传和下载
 * @author Logic Luo
 */
public class ServerThread extends Thread {
    private Socket socket = null;
    /**
     * 默认无参构造函数
     */
    public ServerThread() {}

    /**
     * 以socket为参数的构造函数
     * @param socket
     */
    public ServerThread(Socket socket) {
        this.socket = socket;
    }

    /**
     * 服务器端开始程序
     * @throws IOException
     */
    @Override
    public void run() {
        // 创建服务器端ServerSocket
        try {
            DataInputStream dataInputStream = new DataInputStream(
                    new BufferedInputStream(socket.getInputStream()));

            //接收从服务器端传来的标志位是上传还是下载
            int flag = dataInputStream.readInt();

            //读取传过来的文件名
            String fileName = dataInputStream.readUTF();

            if(0 == flag) {
                receiveFileFromClient(fileName, dataInputStream);
                System.out.println("从Client端接收文件成功!");
            } else {
                DataOutputStream dataOutputStream = new DataOutputStream(
                        new BufferedOutputStream(socket.getOutputStream()));
                transmitFileToClient(fileName, dataOutputStream);
                dataOutputStream.close();
                System.out.println("向Client端传递文件成功!");
            }

            dataInputStream.close();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            //关闭socket
            if(socket != null) {
                try {
                    socket.close();
                } catch (IOException e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                }
            }
        }
    }

    /**
     * 接收从客户端传过来的文件
     * @param fileName 服务器端文件名称
     * @param dataInputStreamReceive 从socket接收数据的输入流
     * @throws IOException
     */
    public void receiveFileFromClient(String fileName, DataInputStream dataInputStream) throws IOException {
        String filePath = Constant.SERVERFOLDER + "/" + fileName;
        DataOutputStream dataOutputStream = new DataOutputStream(
                new BufferedOutputStream(new FileOutputStream(new File(filePath))));
        Transmission transmission = new Transmission(dataInputStream,
                dataOutputStream);
        transmission.transmitData();
        dataOutputStream.close();
    }

    /**
     * 从服务器端向客户端发送文件
     * @param fileName 本地文件名
     * @param dataOutputStreamUpload 向socket发送数据的输出流
     * @throws IOException
     */
    public void transmitFileToClient(String fileName, DataOutputStream dataOutputStream) throws IOException {
        String filePath = Constant.SERVERFOLDER + "/" + fileName;
        DataInputStream dataInputStream = new DataInputStream(
                new BufferedInputStream(new FileInputStream(new File(filePath))));

        Transmission transmission = new Transmission(dataInputStream, dataOutputStream);
        transmission.transmitData();
        dataInputStream.close();
    }

}
