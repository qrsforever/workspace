
public class InterrputTest {
    public static void main(String[] args) {
        System.out.println("InterrputTest main");
        Object obj = new Object();
        Thread t1 = new Thread(new Runnable() {
            @Override
            public void run() {
                synchronized(obj) {
                    try {
                        System.out.println("T1 wait");
                        obj.wait(); // wait 会释放obj对象锁, 所以天t2有机会获取到
                    } catch(InterruptedException e){
                        System.out.println("T1 InterruptedException");
                    }
                }
            }
        });

        Thread t2 = new Thread(new Runnable() {
            @Override
            public void run() {
                synchronized(obj) {
                    try {
                        System.out.println("T2 sleep");
                        Thread.sleep(100000);
                    } catch(InterruptedException e){
                        System.out.println("T2 InterruptedException");
                    }
                }
            }
        }); 

        System.out.println("T1 start thread");
        t1.start();

        System.out.println("T2 start thread");
        t2.start();

        try {
            Thread.sleep(3000);
        } catch (InterruptedException e){
            e.printStackTrace();
        }

        t1.interrupt();
        while (!t1.isInterrupted()) {
            System.out.println("T1 is Interrupted: " + t1.isInterrupted());
            try {
                Thread.sleep(10);
            } catch (InterruptedException e){
                e.printStackTrace();
            }
        }

        t2.interrupt();
        while (!t2.isInterrupted()) {
            System.out.println("T2 is Interrupted: " + t2.isInterrupted());
            try {
                Thread.sleep(10);
            } catch (InterruptedException e){
                e.printStackTrace();
            }
        }
    }
}
