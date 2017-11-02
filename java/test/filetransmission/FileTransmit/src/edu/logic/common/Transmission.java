package edu.logic.common;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;

/**
 * �����ļ�����
 * @author Logic Luo
 */
public class Transmission {
    private DataInputStream sourceStream = null;
    private DataOutputStream destinationStream = null;

    public Transmission(){}

    /**
     * �����������Ĺ��캯��
     * @param sourceStream
     * @param destinationStream
     */
    public Transmission(DataInputStream sourceStream,
            DataOutputStream destinationStream) {
        this.sourceStream = sourceStream;
        this.destinationStream = destinationStream;
    }

    /**
     * ���ݴ���
     * @throws IOException
     */
    public void transmitData() throws IOException {
        int bufferSize = 8192;
        byte[] buffer = new byte[bufferSize]; 
        while(true) {
            int readSize = 0;
            if(sourceStream != null ) {
                readSize = sourceStream.read(buffer);
            }
            if(readSize == -1) {
                break;
            }
            destinationStream.write(buffer, 0, readSize);
        }
        destinationStream.flush();
    }
}
