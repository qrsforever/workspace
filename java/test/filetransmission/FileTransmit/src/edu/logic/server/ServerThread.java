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
 * �����ļ����ϴ�������
 * @author Logic Luo
 */
public class ServerThread extends Thread {
    private Socket socket = null;
    /**
     * Ĭ���޲ι��캯��
     */
    public ServerThread() {}

    /**
     * ��socketΪ�����Ĺ��캯��
     * @param socket
     */
    public ServerThread(Socket socket) {
        this.socket = socket;
    }

    /**
     * �������˿�ʼ����
     * @throws IOException
     */
    @Override
    public void run() {
        // ������������ServerSocket
        try {
            DataInputStream dataInputStream = new DataInputStream(
                    new BufferedInputStream(socket.getInputStream()));

            //���մӷ������˴����ı�־λ���ϴ���������
            int flag = dataInputStream.readInt();

            //��ȡ���������ļ���
            String fileName = dataInputStream.readUTF();

            if(0 == flag) {
                receiveFileFromClient(fileName, dataInputStream);
                System.out.println("��Client�˽����ļ��ɹ�!");
            } else {
                DataOutputStream dataOutputStream = new DataOutputStream(
                        new BufferedOutputStream(socket.getOutputStream()));
                transmitFileToClient(fileName, dataOutputStream);
                dataOutputStream.close();
                System.out.println("��Client�˴����ļ��ɹ�!");
            }

            dataInputStream.close();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            //�ر�socket
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
     * ���մӿͻ��˴��������ļ�
     * @param fileName ���������ļ�����
     * @param dataInputStreamReceive ��socket�������ݵ�������
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
     * �ӷ���������ͻ��˷����ļ�
     * @param fileName �����ļ���
     * @param dataOutputStreamUpload ��socket�������ݵ������
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
