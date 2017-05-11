package com.leeco.learn;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class MainSpring {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ApplicationContext context = new ClassPathXmlApplicationContext("Beans.xml");

		HelloSpring obj = (HelloSpring) context.getBean("hellospring");

		obj.getMessage();
	}

}
