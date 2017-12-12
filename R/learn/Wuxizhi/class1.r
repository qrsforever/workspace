#!/usr/bin/env Rscript

# eg.1 (柱形图)
v = read.table("res/Billianaires.TXT", sep=",", header=T, na.strings="-")
# 返回类型
mode(v)
typeof(v)
par(mfrow=c(1,2))
hist(v$Age, main="", xlab="Age")
hist(v$Net.Worth, main="", xlab="Net Worth")

# eg.2 (沙箱图)
par(mfrow=c(1,1))
w = v[v[,6]=="United States"|v[,6]=="China"|v[,6]=="Japan",]
w[,6] = as.character(w[,6])
boxplot(Age~Country.of.Citizenship, w)

# eg.3 (散点图)
v = read.table("res/g100.txt", sep=",", header=T)
plot(v$Assets, v$Sales, 
     pch=1, col=1, 
     xlab="Assets(Billion $)", 
     ylab="Sales(Billion $)", 
     ylim=c(0, 600), 
     xlim=c(-100, 3000), 
     cex=log(v$Profits))
title("Global 100 Companys' Assets, Sales and log Profits(size of points)")
identify(v$Assets, v$Sales, labels=v$Company)

# eg.4 (饼图), 前10行
# table: 计算频数
w = read.table("res/global2000.TXT", sep=",", header=T)
ws = sort(table(w$Country), de=T)
pie(ws[1:10])
title("Number of Companies Among top 10")

# eg.5 (条形图), 前10行
# cex: character extension (设置字体大小等)
barplot(ws[1:10], cex.names=.8, main="Number of Companies Among top 10")
