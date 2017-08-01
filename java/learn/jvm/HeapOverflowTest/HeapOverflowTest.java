import java.util.List;
import java.util.ArrayList;

public class HeapOverflowTest {

    static class OOMObject{
        byte[] nouse = new byte[10240];
    }

    public static void main(String[] args) {
        List<OOMObject> list = new ArrayList<OOMObject>();
        while (true) {
            list.add(new OOMObject());
            try {
                Thread.sleep(2);
            } catch (InterruptedException e){
                e.printStackTrace();
            }
        }
    }
}

// java -Xmx100M HeapOverflowTest
// jvisualvm
// java.lang.OutOfMemoryError: Java heap space
