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
 * �ͻ�����
 * @author Logic Luo
 */
public class Client {

    /**
     * �ͻ��˿�ʼ����
     * @throws UnknownHostException
     * @throws IOException
     */
    @SuppressWarnings("resource")
    public void start() throws UnknownHostException, IOException {
        while(true) {
            System.out.println("�밴�����¸�ʽ��д���\n�ϴ��ļ���put �����ļ��� �������ļ���\n�����ļ���get �������ļ��� �����ļ���");
            String localFileName = null;
            String remoteFileName = null;
            // �����������������
            Scanner scanner = new Scanner(System.in);
            String command = scanner.nextLine();
            // �������
            String[] commandArray = command.split(" ");
            Socket socket = null;
            int flag = 0;

            // �������
            if(commandArray[0].equals("put")) {
                flag = 0;
                localFileName = commandArray[1];
                remoteFileName = commandArray[2];
            } else {
                flag = 1;
                localFileName = commandArray[2];
                remoteFileName = commandArray[1];
            }

            // ����socket,��������˷����������� 
            socket = new Socket(Constant.HOSTIP, Constant.PORT);

            DataOutputStream dataOutputStream = new DataOutputStream(
                    new BufferedOutputStream(socket.getOutputStream()));

            // ��������˷����ϴ������ر�־
            dataOutputStream.writeInt(flag);
            dataOutputStream.flush();

            // ��������˷���Զ���ļ���
            dataOutputStream.writeUTF(remoteFileName);
            dataOutputStream.flush();

            if(flag == 0) {
                // ��������˴����ļ�
                putFileToServer(localFileName, dataOutputStream);
                System.out.println("�ͻ����ϴ��������");
            } else {
                DataInputStream dataInputStream = new DataInputStream(
                        new BufferedInputStream(socket.getInputStream()));
                getFileFromServer(localFileName, dataInputStream);
                dataInputStream.close();
                System.out.println("�ͻ������ݽ������");
            }
            dataOutputStream.close();
            socket.close();
            System.out.println("File transfer complete");
        }
    }

    /**
     * �ӿͻ�����������ϴ�����
     * @param fileName �ͻ����ļ���
     * @param dataOutputStreamUpload
     * @throws IOException
     */
    public void putFileToServer(String fileName, DataOutputStream dataOutputStream) throws IOException {
        String filePath = Constant.CLIENTFOLDER + "/" + fileName;
        //�����ļ�������
        DataInputStream dataInputStream = new DataInputStream(
                new BufferedInputStream(new FileInputStream(new File(filePath))));
        Transmission transmission = new Transmission(dataInputStream, dataOutputStream);
        transmission.transmitData();
        dataInputStream.close();
    }

    /**
     * �ӷ�������ͻ�����������
     * @param fileName �ͻ����ļ���
     * @param dataInputStreamReceive socket�������ݵ�������
     * @throws IOException
     */
    public void getFileFromServer(String fileName, DataInputStream dataInputStream) throws IOException {
        String filePath = Constant.CLIENTFOLDER + "/" + fileName;
        //�����ļ������
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
