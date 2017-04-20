package com.leeco.learn;

public class Client {
    public static void main(String[] args) {
        Handler h1 = new BossHandler();
        Handler h2 = new ChiefHandler();
        Handler h3 = new CaptainHandler();
        Handler h4 = new EmployeeHandler();
        h4.setSuccessor(h3);
        h3.setSuccessor(h2);
        h2.setSuccessor(h1);

        h4.handlerMessage(0);
        h4.handlerMessage(1);
        h4.handlerMessage(2);
        h4.handlerMessage(3);
    }
}


// 根据个人的职责层层作出符合自己的事
