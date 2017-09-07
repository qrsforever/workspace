#!/bin/bash

# sed -i "s/原字符串/新字符串/g" `grep 原字符串 -rl 所在目录`
# -i 表示inplace edit，就地修改文件
# -r 表示搜索子目录
# -l 表示输出匹配的文件名
# 这个命令组合很强大，要注意备份文件。

echo "12345 hello 67890" >> /tmp/sed-tmp.txt
echo "12345 world 67890" >> /tmp/sed-tmp.txt

echo "原文:"
cat /tmp/sed-tmp.txt
sed -i "s/12345/adbce/g" `grep 12345 -rl /tmp/sed-*.txt`
echo "现文:"
cat /tmp/sed-tmp.txt
