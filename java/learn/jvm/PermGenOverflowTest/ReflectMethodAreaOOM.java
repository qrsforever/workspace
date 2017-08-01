import java.util.List;
import java.util.ArrayList;
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;  

// 测试失败Fail
public class ReflectMethodAreaOOM {

    public interface UserService {
        void server();
    }

    static class UserServiceImpl implements UserService {
        public void server() {
            // do something
            System.out.println("server");
        }
    }

    static class CatchInvocationHandler implements InvocationHandler {
        private Object target;

        public CatchInvocationHandler(Object target) {
            super();
            this.target = target;
        }

        public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
            // 装饰模式
            {
                // before do something
            } 
            Object result = method.invoke(target, args);
            {
                // after do something
            }
            return result;
        }

        public Object getProxy() {
            return Proxy.newProxyInstance(
                    Thread.currentThread().getContextClassLoader() /* 类加载器 */,
                    target.getClass().getInterfaces(), /* target的所有接口 */
                    this /* 自定义的InvocationHandle*/);
        }

    }

    public static void main(String[] args) 
            throws NoSuchMethodException, IllegalAccessException, InstantiationException {
        List<Object> list = new ArrayList<Object>();
        System.getProperties().put("sun.misc.ProxyGenerator.saveGeneratedFiles", true);
        // 该方法不能验证无限加载class, 导致方法区内存溢出
        while (true) {
            UserService userService = new UserServiceImpl();  
            CatchInvocationHandler invocationHandler = new CatchInvocationHandler(userService);  
            UserService proxy = (UserService)invocationHandler.getProxy();  
            proxy.server();
            list.add(proxy);
            try {
                Thread.sleep(200);
            } catch(Exception e){
                e.printStackTrace();
            }
        }
    }
}
