import java.io.File;
import java.net.URL;
import java.net.URLClassLoader;
import java.util.ArrayList;
import java.util.List;

// 测试失败Fail
public class ClassLoaderMethodAreaOOM {

    public static void main(String[] args) {
        URL url = null;
        List<ClassLoader> classLoaderList = new ArrayList<ClassLoader>();
        try {
            url = new File(".").toURI().toURL();
            System.out.println("url = " + url.toString());
            URL[] urls = {url};
            while (true) {
                // JVM在判定两个class是否相同时，不仅要判断两个类名是否相同，而且要判断是否由同一个类加载器实例加载的
                ClassLoader loader = new URLClassLoader(urls);
                classLoaderList.add(loader);
                loader.loadClass("EmptyObject");
                Thread.sleep(10);
            }
        } catch(Exception e){
            e.printStackTrace();
        }
    }
}

// java1.6
// java -XX:PermSize=8m -XX:MaxPermSize=8m ClassLoaderMethodAreaOOM
// java1.8
// java -XX:MetaspaceSize=8m -XX:MaxMetaspaceSize=8m ClassLoaderMethodAreaOOM
