#!/usr/bin/env Rscript

# dpois, ppois, qpois, rposi
# d-密度函数后分布律
# p-分布函数
# q-分布函数的反函数，即给定概率p下，求其下分为点
# r-仿真(产生相同分布随机数)

# eg.1
# Binom distribution
par(mfrow=c(3,3))
for (i in seq(.1, .9, .1)) {
    barplot(dbinom(0:5, 5, i))
    # p == that 使用list里面的变量值变换替换
    title(main=(substitute(p == that, list(that = i))))
}

# eg.2
# Possion distribution
# type = "b": both - 点线
# pch = n: 控制连接点的symbol
plot(dpois(0:20, 3), type="b", pch=15, xlab="k", ylab="p(k)")
points(dpois(0:20, 6), type="b", pch=17)
points(dpois(0:20, 10), type="b", pch=19)
# text 在指定坐标输入txt
text(c(3.5, 6.5, 11.5), c(.18, .14, .09), 
     c(expression(lambda==3), 
       expression(lambda==6),
       expression(lambda==10)))
title(main="Possion Distribution")

# eg.3 理解概率密度, 当连续型变量, 在某个值上的频数, 实际上非常小(因为连续分母很大)
x = rnorm(100000)
par(mfrow=c(2,2))
# hist: 按n分成相等的份, 在该区间的频数和
hist(x, 14, col="blue", xlab="", ylab="", main="Histogram 1")
hist(x, 50, col="blue", axes=FALSE, xlab="", ylab="", main="Histogram 2")
hist(x, 100, col="blue", xlab="", ylab="", main="Histogram 2")

# 正态分布x>4, y接近0 (因为sigma=1, mu=0, 3*sigma --> 99%)
# dnorm 是密度函数, 给定xs, 返回ys
xs = seq(-4, 4, l=1000)
ys = dnorm(xs)
plot(xs, ys, type="l", axes=FALSE, xlab="", ylab="", main="Density")
# 多边形填充
polygon(c(xs[xs>-4]), c(dnorm(c(xs[xs>-4]))), col="blue")
