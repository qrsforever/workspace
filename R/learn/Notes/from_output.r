#!/usr/bin/env Rscript

help(source)
help(sink)

## from file
source("./get_help.r")

## output file,  sink() 结束
sink("/tmp/output.lis")
i = 1:10
## 在sink()执行之前, output内容输出到文件中
outer(i, i, "*")
sink()
