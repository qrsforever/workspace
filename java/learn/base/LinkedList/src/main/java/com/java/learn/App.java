package com.java.learn;

import java.util.LinkedList;
import java.util.NoSuchElementException;

public class App {
    public static void main(String[] args) {
        LinkedList<Integer> list = new LinkedList<Integer>();
        // 1. remove 和 poll 区别
        try {
            // queue为null时, 抛异常
            list.remove();
        } catch(NoSuchElementException e){
            e.printStackTrace();
        }
        // queue为null时, 返回null
        Integer element = list.poll();
        if (element == null)
            System.out.println("queue is null!");

        // 3. 添加操作, list没有queue满的控制, 所以add == offer
        list.add(1);   // == addLast() queue full, throw
        list.offer(2); // == add(); queue full, return null
        list.push(3);  // == addFirst()

        list.add(1, 4);

        System.out.println("list.size = " + list.size());
        System.out.println("list(0) = " + list.get(0));
        System.out.println("list(1) = " + list.get(1));
    }
}

//
//
//
//                                 +----------------+
//                                 |  Collection    |
//                                 +--^-----------^-+
//                                   /             \
//                                  /               \
//                                 /                 \
//                                /                   \
//                       +--------+                +---\------+
//                       |  List  |                |   Queue  |
//                       +--------+                +-----^----+
//                           ^                          |
//                            \                         |
//                             \                        |
//                              \                       |
//                               \               +------+-----+
//                                \              |    Deque   |                    ^ interface
//                                 \             +---^--------+                    |
//                                  \               /                              |
//                                   \             /                               |
// -----------------------------------\-----------/--------------------------------+----
//                                     \         /
//                                      \       /
//                                 +-----\-----/-+
//                                 |  LinkedList |
//                                 +-------------+
//
//
//
