
public class StackOverflowTest {
    private static int level = 0;

    public static long fact(int n) {
        level++;
        return (n < 2) ? 1 : n * fact(n - 1);
    }

    public static void main(String[] args) {
        try {
            System.out.println(fact(1 << 15)); // 递归stack溢出
        } catch(StackOverflowError e){
            System.err.println("recursion level : " + level);
            System.err.println("reported recursion level length : " + e.getStackTrace().length);
        }
    }
}

// 溢出: java StackOverflowTest
// 可以将栈调大防止递归溢出 -Xss3M
