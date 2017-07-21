import java.lang.ref.SoftReference;

public class SoftReferenceTest {

    private SoftReference<byte[]> dataRef = null;

    public SoftReferenceTest() {
        dataRef = new SoftReference<byte[]>(new byte[0]);
        System.out.println("length : " + dataRef.get().length);
    }

    public byte[] readData() {
        byte[] dataArray = dataRef.get();
        System.out.println("dataRef = " + dataArray);
        if (dataArray == null || dataArray.length == 0) {
            System.out.println("NEW SoftReference");
            dataArray = new byte[1024 * 1024];
            dataRef = new SoftReference<byte[]>(dataArray);
        }
        return dataArray;
    }

    public static void main(String[] args) {
        SoftReferenceTest ss = new SoftReferenceTest(); 
        ss.readData();
        try {
            Thread.sleep(3000);
        } catch (InterruptedException e){
            e.printStackTrace();
        }

        // 暂用内存空间, 触发GC操作. 内存不足就会被回收
        byte[] bb = new byte[2 * 1024 * 1024];
        bb = null;
        ss.readData();
    }
}

// 运行: java -verbose:gc -Xmx3M SoftReferenceTest
