package com.leeco.learn.string;

public class StringConstantPool {

	public static void main(String[] args) {
		String s1 = "ConstantString";
		String s2 = "ConstantString";
		String s3 = new String("ConstantString");
		String s4 = new String("ConstantString");
		String s5 = new String("AnotherString");

		// 等价s.toString() s1 -> s5 输出内容相同， 但是s1 == s3是引用比较， 对象不同
        System.out.println("s1 : " + s1);
        System.out.println("s2 : " + s2);  
        System.out.println("s3 : " + s3);
        System.out.println("s4 : " + s4);
        System.out.println("s5 : " + s5);
        
        System.out.println("s1.toString() : " + s1.toString());
        System.out.println("s2.toString() : " + s2.toString());
        System.out.println("s3.toString() : " + s3.toString());
        System.out.println("s4.toString() : " + s4.toString());
        System.out.println("s5.toString() : " + s5.toString());
        
        // 某种程度上hashCode可作为内存地址分析（实际上只是对应关系)
		System.out.println("s1.hashCode() : " + s1.hashCode());  // 相同
		System.out.println("s2.hashCode() : " + s2.hashCode());  // 相同
		System.out.println("s3.hashCode() : " + s3.hashCode());  // 相同
		System.out.println("s4.hashCode() : " + s4.hashCode());  // 相同
		System.out.println("s5.hashCode() : " + s5.hashCode());  // 不同
		
		// 引用地址比较
		if (s1 == s2) 
			System.out.println("s1 == s2");  // True
		if (s3 == s4)
			System.out.println("s3 == s4");  // False
		if (s1 == s3)
			System.out.println("s1 == s3");  // False
		if (s1 == "ConstantString")
			System.out.println("s1 == ConstantString");  // True
		if (s1.equals(s3))
			System.out.println("s1.equals(s3)");  // True

	}

}
