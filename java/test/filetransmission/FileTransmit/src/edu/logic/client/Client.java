package edu.logic.client;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Scanner;

import edu.logic.common.Transmission;
import edu.logic.constant.Constant;

/**
 * 客户端类
 * @author Logic Luo
 */
public class Client {

    /**
     * 客户端开始程序
     * @throws UnknownHostException
     * @throws IOException
     */
    @SuppressWarnings("resource")
    public void start() throws UnknownHostException, IOException {
        while(true) {
            System.out.println("请按照以下格式书写命令：\n上传文件：put 本地文件名 服务器文件名\n下载文件：get 服务器文件名 本地文件名");
            String localFileName = null;
            String remoteFileName = null;
            // 接收命令行输入参数
            Scanner scanner = new Scanner(System.in);
            String command = scanner.nextLine();
            // 命令解析
            String[] commandArray = command.split(" ");
            Socket socket = null;
            int flag = 0;

            // 命令解析
            if(commandArray[0].equals("put")) {
                flag = 0;
                localFileName = commandArray[1];
                remoteFileName = commandArray[2];
            } else {
                flag = 1;
                localFileName = commandArray[2];
                remoteFileName = commandArray[1];
            }

            // 创建socket,向服务器端发送链接请求 
            socket = new Socket(Constant.HOSTIP, Constant.PORT);

            DataOutputStream dataOutputStream = new DataOutputStream(
                    new BufferedOutputStream(socket.getOutputStream()));

            // 向服务器端发送上传或下载标志
            dataOutputStream.writeInt(flag);
            dataOutputStream.flush();

            // 向服务器端发送远程文件名
            dataOutputStream.writeUTF(remoteFileName);
            dataOutputStream.flush();

            if(flag == 0) {
                // 向服务器端传送文件
                putFileToServer(localFileName, dataOutputStream);
                System.out.println("客户端上传数据完成");
            } else {
                DataInputStream dataInputStream = new DataInputStream(
                        new BufferedInputStream(socket.getInputStream()));
                getFileFromServer(localFileName, dataInputStream);
                dataInputStream.close();
                System.out.println("客户端数据接收完成");
            }
            dataOutputStream.close();
            socket.close();
            System.out.println("File transfer complete");
        }
    }

    /**
     * 从客户端向服务器上传数据
     * @param fileName 客户端文件名
     * @param dataOutputStreamUpload
     * @throws IOException
     */
    public void putFileToServer(String fileName, DataOutputStream dataOutputStream) throws IOException {
        String filePath = Constant.CLIENTFOLDER + "/" + fileName;
        //创建文件输入流
        DataInputStream dataInputStream = new DataInputStream(
                new BufferedInputStream(new FileInputStream(new File(filePath))));
        Transmission transmission = new Transmission(dataInputStream, dataOutputStream);
        transmission.transmitData();
        dataInputStream.close();
    }

    /**
     * 从服务器向客户端下载数据
     * @param fileName 客户端文件名
     * @param dataInputStreamReceive socket接收数据的输入流
     * @throws IOException
     */
    public void getFileFromServer(String fileName, DataInputStream dataInputStream) throws IOException {
        String filePath = Constant.CLIENTFOLDER + "/" + fileName;
        //创建文件输出流
        DataOutputStream dataOutputStream = new DataOutputStream(
                new BufferedOutputStream(new FileOutputStream(new File(filePath))));
        Transmission transmission = new Transmission(dataInputStream, dataOutputStream);
        transmission.transmitData();
        dataOutputStream.close();
    }

    public static void main(String[] args) throws Exception {
        new Client().start();
    }
}
