package com.leeco.learn;

public class LeecoMain {
    public static void main(String[] args) {
        WorldChess chess = null;
        chess = ChessFactory.createChess(1);
        System.out.println("CreateChess = " + chess.getCode());
        chess = ChessFactory.createChess(2);
        System.out.println("CreateChess = " + chess.getCode());
        chess = ChessFactory.createChess(1); // 享元模式，不会在创建新的对象， 使用缓存中的
        System.out.println("CreateChess = " + chess.getCode());
    }
}
