import java.util.List;
import java.util.ArrayList;

// 方法区溢出: 运行时常量池溢出
public class RuntimeConstantPoolOOM {

    public static void main(String[] args) {
        // 防止GC回收方法区
        List<String> list = new ArrayList<String>();    
        int i = 0;
        while (true) {
            // String.intern 本地方法
            list.add(String.valueOf(i++).intern());
        }
    }
}

// jdk1.6
// java -XX:MaxPermSize=32m	
// java.lang.OutOfMemoryError: PermGen space
 
// jdk1.8 (字符串常量放到了heap区)
// java.lang.OutOfMemoryError: Java Heap space
