---

title: Docker介绍
date: 2018-04-12 10:35:42
tags: [ Docker ]
categories: [ Tools ]

---

<!-- vim-markdown-toc GFM -->

* [简介](#简介)
    * [基本概念](#基本概念)
    * [如何使用](#如何使用)
    * [Dockerfile](#dockerfile)
* [FQA](#fqa)

<!-- vim-markdown-toc -->

简介
====
Docker 是个划时代的开源项目，它彻底释放了计算虚拟化的威力，极大提高了应用的维护效率，降低了云计算应用开发的成本！ 
[参考](https://yeasy.gitbooks.io/docker_practice/content/)

基本概念
--------

Docker 包括三个基本概念
* 镜像(Image)
    最小root文件系统
* 容器(Container)
    镜像运行的实体, 容器可以被创建/启动/停止/删除/暂停
* 仓库(Repository)
    如果需要在其他服务器上运行, 需要存储转发

如何使用
--------

1. 获取镜像

  ```:-
  docker pull [选项] [Docker Registry 地址[:端口号]/]仓库名[:标签]
  ```

  比如,获取官方镜像 library/ubuntu 仓库中标签为 16.04 的镜像: `docker pull ubuntu:16.04`

2. 运行容器 
  ```:-
  docker run -it --rm \
      ubuntu:16.04 \
      bash
  ```

3. 列出镜像
  ```:-
  docker image ls
  ```

Dockerfile
----------

FQA
===

1. TLS handshake timeout
  使用国内仓库daocloud
  ```bash
   export OPTS="$OPTS --registry-mirror=http://f2d6cb40.m.daocloud.io"
   echo "DOCKER_OPTS=\"\$DOCKER_OPTS $OPTS\"" | sudo tee -a /etc/default/docker
   sudo service docker restart
  ```
  如果没有/etc/default/docker修改/etc/docker/daemon.json 
  ```
    {
        "registry-mirrors": ["http://ef017c13.m.daocloud.io"],
        "live-restore": true
    }
  ```

2. 非root执行docker
  因为docker使用socket需要root权限
  ```bash
   sudo groupadd docker
   sudo gpasswd -a ${USER} docker
   sudo service docker restart
  ```

3. 修改默认存储镜像目录
   ```bash
   sudo service docker stop
   dockerd --help
   export OPTS="$OPTS --data-root=/data/projects/docker"
   echo "DOCKER_OPTS=\"\$DOCKER_OPTS $OPTS\"" | sudo tee -a /etc/default/docker
   sudo service docker start
   docker info
   ```

TODO
====

查IP ??
docker inspect -f='{{.NetworkSettings.IPAddress}}' $(docker ps -a -q)

查看网络类型

docker network ls

see 0docker
