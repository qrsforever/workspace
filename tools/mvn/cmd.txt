mvn eclipse:eclipse -Dwtpversion=2.0
mvn -DdownloadSources=true -DdownloadJavadocs=true -DoutputDirectory=target/eclipse-classes eclipse:eclipse
mvn dependency:sources
mvn mybatis-generator:generate 
mvn clean install -DskipTests 
