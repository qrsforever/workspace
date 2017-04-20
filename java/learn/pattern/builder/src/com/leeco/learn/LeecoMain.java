package com.leeco.learn;

public class LeecoMain {
   public static void main(String[] args) {
       LeecoBuilder builder = new LeecoBuilder();
       LeecoPC pc = builder.build();
       pc.showDetails();
       System.out.println("PC price: " + pc.getPrices());
   } 
}

// 零件接口 零件实现 建造物 建造者
