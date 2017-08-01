export JAVA_HOME=/data/opt/jdk/jdk1.7.0_80
export JRE_HOME=$JAVA_HOME/jre
export CLASSPATH=.:$JAVA_HOME/lib:$JRE_HOME/lib
export PATH=$JAVA_HOME/bin:$PATH

# java -XX:MaxPermSize=100m RuntimeConstantPoolOOM
