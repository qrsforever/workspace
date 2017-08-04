import java.lang.reflect.Method;
import net.sf.cglib.proxy.Enhancer;
import net.sf.cglib.proxy.MethodInterceptor;
import net.sf.cglib.proxy.MethodProxy;

// OK
public class CglibProxyClassOOM {
    public static void main(String[] args) {
        while (true) {
            Enhancer enhancer = new Enhancer();
            enhancer.setSuperclass(CglibProxyClassOOM.class);
            // 不要缓存
            enhancer.setUseCache(false);
            enhancer.setCallback(new MethodInterceptor() {
                public Object intercept(Object o, Method method, Object[] objects, MethodProxy methodProxy) throws Throwable {
                    return methodProxy.invokeSuper(o, objects);
                }
            });
            enhancer.create();
        }
    }
}

// javac -classpath /home/lidong/.m2/repository/cglib/cglib-nodep/3.1/cglib-nodep-3.1.jar 
// export CLASSPATH=/home/lidong/.m2/repository/cglib/cglib-nodep/3.1/cglib-nodep-3.1.jar:$CLASSPATH
// jdk1.7 Args: -XX:PermSize=10M -XX:MaxPermSize=10M
// jdk1.8 Args: -XX:MaxMetaspaceSize=10M
// java.lang.OutOfMemoryError: Metaspace


