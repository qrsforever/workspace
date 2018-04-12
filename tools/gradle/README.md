---

title: Gradle使用配置
date: 2018-03-29 17:41:22
tags: [ Gradle ]
categories: [ Tools ]

---

<!-- vim-markdown-toc GFM -->

* [介绍](#介绍)
    * [Gradle和Gradlew区别](#gradle和gradlew区别)
    * [生成gradlew](#生成gradlew)
    * [执行wrapper任务](#执行wrapper任务)
    * [设置Wrapper版本](#设置wrapper版本)
* [配置文件](#配置文件)
    * [自动编译配置](#自动编译配置)
    * [运行环境配置](#运行环境配置)
    * [子项目包含配置](#子项目包含配置)
    * [本地配置文件](#本地配置文件)
    * [全局配置](#全局配置)
* [常用命令参数及解释](#常用命令参数及解释)
    * [常用命令](#常用命令)
    * [快速构建命令](#快速构建命令)
    * [指定构建目标命令](#指定构建目标命令)
    * [构建并安装调试命令](#构建并安装调试命令)
    * [查看包依赖](#查看包依赖)
    * [其他命令](#其他命令)
* [工程目录](#工程目录)
    * [Native包](#native包)

<!-- vim-markdown-toc -->

<!-- more -->

介绍
====

Gradle和Gradlew区别
--------------------

Gradlew = Gradle + Wrapper

生成gradlew
-----------

```bash:-
gradle init wrapper
```

执行wrapper任务
---------------

```bash:-
gradle wrapper
```

设置Wrapper版本
---------------

1. 通过命令

  ```bash:-
  gradle wrapper --gradle-version 4.0 [--distribution-type all|bin]
  ```

2. 通过修改`gradle/wrapper/gradle-wrapper.properties`文件`distributionUrl`来实现

3. 并且如果向使用本机或者内网gradle, 可以设置`distributionUrl`指向地址

  ```
  distributionUrl=file:///data/opt/gradle/gradle-4.6-bin.zip
  ```

*gradlew会把`distributionUrl`指定版本下载到`${USER_HOME/.gradle/wrapper/dists`*

配置文件
========

自动编译配置
------------

build.gradle

运行环境配置
------------

gradle.properties

子项目包含配置
--------------

setting.gradle

  ```:-
  project
  ├─── setting.gradle
  ├─── build.grade
  ├─── app
  │    └─── build.gradle
  └─── libraries
       ├─── library1
       │    └─── build.gradle
       └─── library2
            └─── build.gradle
  ```

  `include ':app', ':libraries:library1', ':libraries:library2'`

  ```:-1
  dependencies {
         compile project(':libraries:library1')
  }
  ```

本地配置文件
------------

local.properties

全局配置
--------

init.gradle


常用命令参数及解释
==================

常用命令
--------

1. 查看所有任务

  ```bash:-
   gradlew tasks --all
   gradle -q tasks
   ```

2. 对某个module [moduleName] 的某个任务[TaskName] 运行

  ```bash:-
   gradlew :moduleName:taskName
  ```

快速构建命令
-----------

1. 查看构建版本

  ```bash:-
  gradlew -v
  ```

2. 清除build文件夹

  ```bash:-
  gradlew clean
  ```

3. 检查依赖并编译打包

  ```bash:-
  gradlew build
  ```

4. 编译并打印日志

  ```bash:-
  gradlew build --info
  ```

5. 调试模式构建并打印日志

  ```bash:-
  gradlew build --info --debug --stacktrace
  ```

6. 强制更新最新依赖，清除构建并构建

  ```bash:-
  gradlew clean --refresh-dependencies build
  ```

7. unit测试和instrumentation测试

  ```bash:-
  gradlew check
  ```

**注意build = check + assemble: 把debug、release环境的包都打出来的**


指定构建目标命令
---------------

1. 编译并打Debug/Release包

  ```bash:-
  gradlew assembleDebug
  gradlew aD

  gradlew assembleRelease
  gradlew aR
  ```
2. Release模式 test 渠道打包

  ```bash:-
  gradlew assembleTestRelease
  ```

3. debug release模式全部打包

  ```bash:-
  gradlew assemble
  ```

构建并安装调试命令
-----------------

1. 编译app module 并打Debug包

  ```bash:-
  gradlew install app:assembleDebug
  ```

2. Debug/Release模式打包并安装

  ```bash:-
  gradlew installDebug
  gradlew iD

  gradlew installRelease
  gradlew iR
  ```

3. 卸载Debug/Release模式包

  ```bash:-
  gradlew uninstallDebug
  gradlew uD

  gradlew uninstallRelease
  gradlew uR
  ```

查看包依赖
----------

1. 显示所有依赖

  ```bash:-
  gradlew dependencies
  ```

2. 编译时的依赖库

  ```bash:-
  gradlew app:dependencies --configuration compile
  ```

3. 运行时的依赖库

  ```bash:-
  gradlew app:dependencies --configuration runtime
  ```

其他命令
--------

1. 排除任务`-x`

  ```bash:-
  gradle dist -x test
  ```

2. 显示执行顺序`-m`

  ```bash:-
  gradle dist test -m
  ```

3. 使用离线模式 (如果本地有缓存,就不去联网检查更新依赖)

  ```bash:-
  gradlew aDR --offline
  ```

  *aDR = assemble develop realease, 项目有几个产品类型:develop, test, official*

4. 守护进程

  ```bash:-
  gradle build --daemon
  ```

5. 并行编译模式

  ```bash:-
  gradle build --parallel --parallel-threads=N
  ```

6. 按需编译模式

  ```bash:-
  gradle build --configure-on-demand
  ```

7. 不使用snapshot依赖仓库

  ```bash:-
  gradlew clean aDR
  ```

工程目录
========

Native包
--------

  ```:-
  app
     ├── AndroidManifest.xml
     └── jniLibs
         ├── armeabi
         │   └── nativelib.so
         ├── armeabi-v7a
         │   └── nativelib.so
         ├── mips
         │   └── nativelib.so
         └── x86
             └── nativelib.so
  ```

TODO
====

1. 依赖检测(module:app), 然后使用exclude module排除冲突
    gradle -q app:dependencies
    
