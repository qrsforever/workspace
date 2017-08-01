export JAVA_HOME=/data/opt/jdk/jdk1.8.0_141
export JRE_HOME=$JAVA_HOME/jre
export CLASSPATH=.:$JAVA_HOME/lib:$JRE_HOME/lib
export PATH=$JAVA_HOME/bin:$PATH

# 本地内存不断增大, 但是metaspace空间并没有持续增加
# java -XX:MaxMetaspaceSize=100m RuntimeConstantPoolOOM
