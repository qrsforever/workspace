package com.java.learn;

import org.dom4j.Document;
import org.dom4j.Element;
import org.dom4j.io.SAXReader;

import java.io.ByteArrayInputStream;
import java.util.List;

public class App 
{
    public static void main( String[] args ) throws Exception {
        SAXReader reader = new SAXReader();
        String xml = "<books><book><author>Thomas</author><title>Java从入门到放弃</title><publisher>UCCU</publisher>" +
            "</book><book><author>小白</author><title>MySQL从删库到跑路</title><publisher>GoDie</publisher></book>" +
            "<book><author>PHPer</author><title>BestPHP</title><publisher>PHPchurch</publisher></book></books>";
        Document document = reader.read(new ByteArrayInputStream(xml.getBytes("utf-8")));
        Element root = document.getRootElement();
        List<Element> childElements = root.elements();

        for (Element child : childElements) {
            List<Element> books = child.elements();
            for (Element book : books) {
                String name = book.getName();
                String text = book.getText();
                System.out.println(name + ":" + text);
            }
        }
        Element book2 = childElements.get(1);
        Element author = book2.element("author");
        Element title = book2.element("title");
        Element publisher = book2.element("publisher");
        System.out.println("作者：" + author.getText());
        System.out.println("书名：" + title.getText());
        System.out.println("出版社："+publisher.getText());
    }
}
