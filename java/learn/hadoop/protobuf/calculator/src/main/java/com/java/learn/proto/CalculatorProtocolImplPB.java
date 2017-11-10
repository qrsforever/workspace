package com.java.learn.proto;

import com.google.protobuf.RpcController;
import com.google.protobuf.ServiceException;
import com.java.learn.proto.CalculatorProtocolProtos.CalculatorRequestProto;
import com.java.learn.proto.CalculatorProtocolProtos.CalculatorResponseProto;

import com.java.learn.ICalculator;

public class CalculatorProtocolImplPB implements CalculatorProtocolPB {

    private ICalculator server = null;

    public CalculatorProtocolImplPB(ICalculator real) {
        this.server = real;
    }

    @Override
    public CalculatorResponseProto add(RpcController controller, CalculatorRequestProto request)
            throws ServiceException {
        int result = server.add(request.getNum1(), request.getNum2());
        return CalculatorResponseProto.newBuilder().setResult(result).build();
    }

    @Override
    public CalculatorResponseProto minus(RpcController controller, CalculatorRequestProto request)
            throws ServiceException {
        int result = server.minus(request.getNum1(), request.getNum2());
        return CalculatorResponseProto.newBuilder().setResult(result).build();
    }
}
