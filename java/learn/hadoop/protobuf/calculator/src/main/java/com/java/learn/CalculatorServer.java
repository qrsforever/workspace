package com.java.learn;

import com.google.protobuf.BlockingService;
import com.google.protobuf.Descriptors.MethodDescriptor;
import com.google.protobuf.Message;
import com.java.learn.proto.CalculatorProtocolImplPB;
import com.java.learn.proto.CalculatorProtocolProtos.CalculatorProtocolService;
import com.java.learn.proto.CalculatorProtocolProtos.CalculatorRequestProto;

public class CalculatorServer implements ICalculator, ICallMethod {

    private RPCServer server = null;
    BlockingService pbService = null;

    public CalculatorServer() {
        // 协议解析实体类
        CalculatorProtocolImplPB implPB = new CalculatorProtocolImplPB(this);
        // 服务, 不负责具体方法协议的解析实现
        pbService  = CalculatorProtocolService.newReflectiveBlockingService(implPB);

        // 可以不采用上面的方式, 自己解析request,调用add/minus返回response
    }

    public void init(int port) {
        // 监听线程
        server = new RPCServer(this, port);
        server.start();
    }

    @Override
    public int add(int a, int b) {
        return a + b;
    }

    @Override
    public int minus(int a, int b) {
        return a - b;
    }

    public byte[] call(int method, byte[] data) {
        try {
            Message request = CalculatorRequestProto.parseFrom(data);
            MethodDescriptor methodDescriptor = null;
            switch(method) {
                case OperatorConstants.ADD:
                    methodDescriptor = pbService.getDescriptorForType().findMethodByName("add");
                    break;
                case OperatorConstants.MINUS:
                    methodDescriptor = pbService.getDescriptorForType().findMethodByName("minus");
                    break;
                default:
                    return new byte[1];
            }
            Message response = pbService.callBlockingMethod(methodDescriptor, null, request);
            return response.toByteArray();
        } catch(Exception e) {
            e.printStackTrace();
        }
        return new byte[1];
    }

    public static void main(String[] args) {
        new CalculatorServer().init(9903);
    }
}
