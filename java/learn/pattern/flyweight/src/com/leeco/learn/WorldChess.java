package com.leeco.learn;

public class WorldChess {

    private int mCode;
    @SuppressWarnings("unused")
    private int mSize;
    @SuppressWarnings("unused")
    private int mHeight;

    /**
     * @param code
     * @param size
     * @param height
     */
    public WorldChess(int code, int size, int height) {
        this.mCode = code;
        this.mSize = size;
        this.mHeight = height;
        System.out.println("New chess: " + code + " " + size + " " + height);
    }

    public int getCode() {
        return mCode;
    }
    
}
