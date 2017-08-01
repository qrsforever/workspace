
import java.nio.Buffer;
import java.nio.ByteBuffer;  
import java.util.ArrayList;
import java.util.List;

public class DirectMemoryOOM {
    public static void main(String[] args) {
        List<Buffer> buffers = new ArrayList<Buffer>();
        int i = 0;
        while (true) {
            //打印当前第几次
            System.out.println(++i);
            //通过不断申请直接缓存区内存消耗直接内存
            buffers.add(ByteBuffer.allocateDirect(1024*1024)); //每次申请1M
        }
    }
}

// java.lang.OutOfMemoryError: Direct buffer memory
// java -XX:MaxDirectMemorySize=30M DirectMemoryOOM
