## 仓库

    https://repo.maven.apache.org/maven2

可以先到这个link中查找自己需要软件的最近版本


mvn eclipse:eclipse -Dwtpversion=2.0
mvn -DdownloadSources=true -DdownloadJavadocs=true -DoutputDirectory=target/eclipse-classes eclipse:eclipse
mvn dependency:sources
mvn mybatis-generator:generate 
mvn clean install -DskipTests 


## 代码框架模块
<!-- mvn archetype:generate -DarchetypeGroupId=com.hivemq -DarchetypeArtifactId=hivemq-extension-archetype -DarchetypeVersion=4.0.0 -->

    -DarchetypeGroupId
    -DarchetypeArtifactId
    -DarchetypeVersion

根据模块自动生成代码

## 执行

    mvn exec:java -Dexec.mainClass="com.java.learn.App"
