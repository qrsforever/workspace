learn:
    (android)
    https://blog.csdn.net/mq2553299/article/details/73065745 (1,2,3,4)
	https://blog.csdn.net/weishenhong/article/details/81256314
    (java)
(✓) http://bisaga.com/blog/programming/dependency-injection-with-dagger-2
    http://www.vogella.com/tutorials/Dagger/article.html#exercise_daggerintro_modules

dagger(匕首)

降低类类耦合性 (dagger2 dependency injection)

@Module

Used on classes which contains methods annotated with @Provides.

@Provides

Can be used on methods in classes annotated with @Module and is used for methods which provides objects for dependencies injection.

@Singleton

Single instance of this provided object is created and shared.

@Component

Used on an interface. This interface is used by Dagger 2 to generate code which uses the modules to fulfill the requested dependencies.
