class LinkTest {
    public static void main(String[] args) {
        // 实验一 javac *.java 之后删除ToBeLinked.class, 程序正常运行
        ToBeLinked tobelink = null; 

        // 实验二 javac *.java 之后删除ToBeLinked.class, 程序报"java.lang.NoClassDefFoundError: ToBeLinked"
        // ToBeLinked tobelink = new ToBeLinked(); 
        System.out.println("Test Link");
    }
}
