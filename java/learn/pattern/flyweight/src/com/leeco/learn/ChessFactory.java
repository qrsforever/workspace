package com.leeco.learn;

import java.util.HashMap;
import java.util.Map;

public class ChessFactory {

    // private Map<int, WorldChess> mChesses = null; // 错误 Map只接受非基本数据元素
    private static Map<Integer, WorldChess> mChesses = new HashMap<Integer, WorldChess>();

    public static WorldChess createChess(int code) {
        WorldChess c = mChesses.get(code);
        if (c == null) {
            c = new WorldChess(code, 10, 2);
            mChesses.put(code, c);
        }
        return c;
    }
}
