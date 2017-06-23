#!/bin/bash

# 参考
# http://blog.csdn.net/uq_jin/article/details/51487439

# 主机名	      ip	          安装的软件	            进程
# master	192.168.1.102	jdk、hadoop	            NN、DFSZKFailoverController
# node1	    192.168.1.201	jdk、hadoop	            NN、DFSZKFailoverController
# node2	    192.168.1.202	jdk、hadoop	            RM
# node3	    192.168.1.203	jdk、hadoop、zookeeper	DN、NM、journalnode
# node4	    192.168.1.204	jdk、hadoop、zookeeper	DN、NM、journalnode
# node5	    192.168.1.205	jdk、hadoop、zookeeper	DN、NM、journalnode

# 拷贝公钥到其他机器
# ssh-copy-id ip

# export VAGRANT_DOTFILE_PATH=/system/vagrant" 
# vagrant up node1 node2 node3 node4 node5"

HADOOP_HOME=/data/opt/hadoop/hadoop-2.8.0
REMOTE_DIR=$PWD/remote
WS_DIR=/home/lidong/workspace

if [[ ! -d $WS_DIR/hadoop ]]
then
    mkdir -p $WS_DIR/hadoop/tmp
fi

# master机 Hadoop配置
cd $HADOOP_HOME

if [[ ! -f etc.tar.gz ]]
then
    tar zcf etc.tar.gz etc
fi
rm -rf etc
rm -rf logs
tar zxf etc.tar.gz

cp -aprf $REMOTE_DIR/common/hadoop/etc/* etc/hadoop

cd -

#////////////////////////////////

# 1. 启动zookeeper（在node3、4、5 )
#     ./bin/zkService.sh start
# 
# 2. 启动journal node（在node3、4、5）
#     ./sbin/hadoop-daemon.sh start journalnode
# 
# 3. 格式化HDFS（namenode）第一次要格式化（在master, node1中任意一台）
#     ./bin/hdfs namenode -format (将tmp拷贝到另一台namenode)
# 
# 4. 格式化 zk（在master即可）
#     ./bin/hdfs zkfc -formatZK
#
# 5. 启动zkfc来监控NN状态（在master, node1）
#    ./sbin/hadoop-daemon.sh start zkfc
#
# 6. 启动HDFS（namenode）（在master即可）
#    ./sbin/start-dfs.sh
#
# 7. 启动YARN（MR）（在node2即可）
#    ./sbin/start-yarn.sh

#////////////////////////////////

# 等待其他node， 以及相应的服务都启动后， 执行
# $HADOOP_HOME/bin/hdfs namenode -format
# scp $WS_DIR/hadoop/tmp node1:workspace/hadoop
# zkfc 机制更多了解 https://segmentfault.com/a/1190000004169627
# $HADOOP_HOME/bin/hdfs zkfc -formatZK


# jps
# http://master:50070/
# http://node2:8088
