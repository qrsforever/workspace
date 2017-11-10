package com.java.learn;

import java.io.DataInputStream;  
import java.io.DataOutputStream;  
import java.io.IOException;  
import java.net.Socket; 
import java.util.Random; 

import com.java.learn.proto.CalculatorProtocolProtos.CalculatorRequestProto;
import com.java.learn.proto.CalculatorProtocolProtos.CalculatorResponseProto;

import com.java.learn.OperatorConstants;

public class CalculatorClient implements ICalculator {
    private int port;

    public CalculatorClient(int port) {
        this.port = port;
    }

    public int doOper(int op, int a, int b) {
        Socket sock = null;
        DataInputStream input = null;
        DataOutputStream output = null;

        try {
            sock = new Socket("localhost", port);
            input = new DataInputStream(sock.getInputStream());
            output = new DataOutputStream(sock.getOutputStream());

            CalculatorRequestProto request = CalculatorRequestProto.newBuilder()
                // .setMethodname(method)
                .setNum1(a)
                .setNum2(b)
                .build();

            byte[] bytes = request.toByteArray();
            output.writeInt(op);
            output.writeInt(bytes.length);  // Request bytes
            output.write(bytes);
            output.flush();

            int length = input.readInt(); 
            byte[] data = new byte[length];
            int count = input.read(data);
            if (count != length) {
                System.err.println("Error!");
            }
            
            CalculatorResponseProto response = CalculatorResponseProto.parseFrom(data);
            return response.getResult();
        } catch(Exception e) {
            System.err.println("Error: " + e.getMessage());
        } finally {
            try {
                input.close();
                output.close();
                sock.close();
            } catch(IOException e){
                System.err.println("Error: " + e.getMessage());
            }
        }
        return 0;
    }

    @Override
    public int add(int a, int b) {
        return doOper(OperatorConstants.ADD, a, b);
    }

    @Override
    public int minus(int a, int b) {
        return doOper(OperatorConstants.MINUS, a, b);
    }

    public static void main(String[] args) {
        Random rand = new Random();  
        CalculatorClient client = new CalculatorClient(9903);
        int a = rand.nextInt(100);
        int b = rand.nextInt(100);
        System.out.println(a + " + " + b + " = " + client.add(a, b));
        System.out.println(a + " - " + b + " = " + client.minus(a, b));
    }
}
