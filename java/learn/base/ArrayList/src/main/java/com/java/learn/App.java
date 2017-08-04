package com.java.learn;

import java.util.ArrayList;
import java.util.Iterator;

public class App {
    public static void main(String[] args) {
        // 可以不指定容量, 默认是10, 并且会根据1.5倍原大小grow
        ArrayList<Integer> list = new ArrayList<Integer>(5);
        list.add(1);
        list.add(2);
        list.add(0, 3);
        System.out.println("list.get(0) = " + list.get(0));
        System.out.println("list.get(1) = " + list.get(1));
        System.out.println("list.get(2) = " + list.get(2));

        list.remove(0); // 删除方式: 下标/对象 == list.remove(new Integer(3));

        Iterator<Integer> it = list.iterator();
        while (it.hasNext()) {
            if (it.next().equals(1))
                it.remove();  // 这里并没有破坏集合的结构性, ArrayList内部类Itr实现了remove
        }

        System.out.println("list.size = " + list.size());
    }
}

//
//
//                       +-------------+
//                       |  Iterable   |
//                       +-----^-------+
//                             |
//                             |   iterator()
//                             |
//                    +--------------+
//                    |  Collection  |
//                    +---^----------+
//                         \
//                          \
//                          |
//                     +----------+
//                     |   List   |
//                     +--------^-+
//                              |
//                              |
//                      +--------------+
//                      |              |
//                      |   ArrayList  |
//                      |              |
//                      +--------------+
//
