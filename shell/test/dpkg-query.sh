#!/bin/bash

# -s：查询软件包的状态信息；
# -L：显示软件包所安装的文件列表；
# -S：从安装的软件包中查询文件；
# -w：显示软件包信息；
# -c：显示软件包的控制文件路径；
# -p：显示软件包的细节。

dpkg-query -W --showformat='${Package}' nfs-kernel-server
