package com.leeco.learn.spring.helloworld;

public class HelloWorldService {
	private HelloWorld helloWorld;

	public HelloWorldService() {

	}

	public void setHelloWorld(HelloWorld helloWorld) {
		System.out.println("setHeloWorld");
		this.helloWorld = helloWorld;
	}

	public HelloWorld getHelloWorld() {
		return this.helloWorld;
	}
}
