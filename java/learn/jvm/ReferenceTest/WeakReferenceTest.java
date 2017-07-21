import java.lang.ref.WeakReference;

public class WeakReferenceTest {
    public static void main(String[] args) {
        System.out.println("Start!");

        WeakReference<Object> oo = new WeakReference<Object>(new Object()); 
        new Thread(new Runnable() {
            @Override
            public void run() {
                System.gc(); // GC到来, 不管有没有内存, 都会清理弱引用对象
            }
        }).start();
        while (true) {
            if (oo.get() == null) {
                System.out.println("GC Object has been collected");
                break;
            }
        }

        System.out.println("End!");
    }
}

// 运行: java -verbose:gc -XX:+PrintGCTimeStamps -XX:+PrintGCDetails WeakReferenceTest
