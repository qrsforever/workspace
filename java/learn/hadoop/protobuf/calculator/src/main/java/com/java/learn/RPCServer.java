package com.java.learn;

import java.io.DataInputStream;  
import java.io.DataOutputStream;  
import java.io.IOException;  
import java.net.*;

public class RPCServer extends Thread {
    private ICallMethod callService = null;
    private int port = 9093;
    private ServerSocket ss = null;

    public RPCServer(ICallMethod call, int port) {
        super();
        this.callService = call;
        this.port = port;
    }

    @Override
    public void run() {
        Socket clientSock = null;
        DataInputStream input = null;
        DataOutputStream output = null;
        while(true) {
            try {
                ss = new ServerSocket(port);
                clientSock = ss.accept();
                input = new DataInputStream(clientSock.getInputStream());
                output = new DataOutputStream(clientSock.getOutputStream());

                int method = input.readInt();
                int length = input.readInt(); // Request bytes
                byte[] data = new byte[length];
                int readCount = input.read(data);
                if (length != readCount) {
                    System.err.println("Error!");
                }
                byte[] result = callService.call(method, data);
                output.writeInt(result.length);
                output.write(result);
                output.flush();
            } catch(Exception e){
                // e.printStackTrace();
            } finally {
                try {
                    input.close();
                    output.close();
                    ss.close();
                } catch(IOException e){
                    e.printStackTrace();
                }
            }
        }
    }
}

