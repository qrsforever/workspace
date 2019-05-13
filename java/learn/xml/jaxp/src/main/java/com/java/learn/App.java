package com.java.learn;

import java.io.File;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

public class App {
    public static void main(String[] args) {
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        try {
            DocumentBuilder builder = factory.newDocumentBuilder();
            Document document = builder.parse(App.class.getResourceAsStream("/app.xml"));
            NodeList itemList = document.getElementsByTagName("item");
            for(int i = 0; i < itemList.getLength(); i ++){
                Element stuElm = (Element)itemList.item(i);
                String number = stuElm.getAttribute("id");
                System.out.println("学号:" + number);
                NodeList childrenList = stuElm.getChildNodes();
                int length = childrenList.getLength();
                for(int j = 0; j < length; j ++) {
                    Node node = childrenList.item(j);
                    if(node.getNodeType() == Node.ELEMENT_NODE){
                        Element child = (Element) node;
                        switch (child.getNodeName()) {
                            case "name":
                                String name = child.getTextContent();
                                System.out.println("姓名:" + name);
                                break;
                            case "age":
                                String age = child.getTextContent();
                                System.out.println("年龄:" + age);
                                break;
                            case "sex":
                                String sex = child.getTextContent();
                                System.out.println("性别:" + sex);
                                break;
                            default:
                                break;
                        }
                    }
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
