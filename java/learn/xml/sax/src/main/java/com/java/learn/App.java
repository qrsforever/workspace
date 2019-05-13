package com.java.learn;

import java.io.File;

import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;

import org.xml.sax.Attributes;
import org.xml.sax.SAXException;
import org.xml.sax.helpers.DefaultHandler;

import java.util.ArrayList;
import java.util.List;

public class App {

    public class Student {
        public String id;
        public String name;
        public Integer age;
        public String sex;
        public String toString() {
            return "student(" + id + ", " + name + ", " + age + ", " + sex + ")";
        }
    }

    public static AppHandler handler = null;

    public AppHandler getHandler() {
        if (handler == null)
            handler = new AppHandler();
        return handler;
    }

    public class AppHandler extends DefaultHandler {

        private List<Student> studentsList;

        private Student student;
        private String tag;

        @Override
        public void startDocument() throws SAXException {
            System.out.println("文档开始解析");
            studentsList = new ArrayList<>();
        }

        @Override
        public void startElement(String uri, String localName, String qName,
                Attributes attributes) throws SAXException {
            System.out.println("元素解析开始(" + uri + ", " + localName + ", " + qName + ")");
            if (null == qName)
                return;
            tag = qName;

            if (qName.equals("item")) {
                student = new Student();
                student.id = attributes.getValue("id");
            }
        }

        @Override
        public void characters(char[] ch, int start, int length) throws SAXException {
            String str = new String(ch, start, length);
            str = str.trim();
            if (str.length() == 0 || null == tag)
                return;

            switch (tag) {
                case "name":
                    student.name = str;
                    break;
                case "age":
                    student.age = Integer.valueOf(str);
                    break;
                case "sex":
                    student.sex = str;
                    break;
                default:
                    ;
            }
        }

        @Override
        public void endElement(String uri, String localName, String qName) throws SAXException {
            System.out.println("元素解析结束(" + uri + ", " + localName + ", " + qName + ")");
            if (qName.equals("item")) {
                studentsList.add(student);
            }
            tag = null;
        }

        @Override
        public void endDocument() throws SAXException {
            System.out.println("文档解析结束");
            for (Student item : studentsList) {
                System.out.println(item);
            }
        }
    }

	public static void main(String[] args) {
		SAXParserFactory factory = SAXParserFactory.newInstance();
		try {
			SAXParser parser = factory.newSAXParser();
			parser.parse(App.class.getResourceAsStream("/app.xml"), new App().getHandler());
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
