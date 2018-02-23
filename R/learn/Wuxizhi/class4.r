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

# eg.4 正态分布 不同值, 形状
xs = seq(-5, 5, .001)
par(mfrow=c(1,1))
ys1 = dnorm(xs, mean=-2, sd = .5)
ys2 = dnorm(xs, mean=0, sd = 1)
# lty: line type
plot(xs, ys1, type="l", lty=2, xlab="", ylab="")
lines(xs, ys2)
text(c(-2, 0), c(.3, .2), c("N(-2, 0.5)", "N(0,1)"))

# eg.5 pdf 密度函数积分(r1 --> r2)
xs = c(seq(-4, 4, length=1000))
ys = dnorm(xs)

r1 = 0.51
r2 = 1.57

xs2 = c(r1, r1, xs[xs>r1&xs<r2], r2, r2)
ys2 = dnorm(c(r1, xs[xs>r1&xs<r2], r2))
ys2 = c(0, ys2, 0)

par(mfrow=c(1,1))
plot(xs, ys, type="l", ylab=expression(phi(x)))
# 画底下一条线
abline(h = 0)
polygon(xs2, ys2, col="gray")


# eg6. 卡方分布
xs = seq(0, 10, l=1000)
ys1 = dchisq(xs, 2)
ys2 = dchisq(xs, 3)
ys3 = dchisq(xs, 5)

par(mfrow=c(1,1))
plot(xs, ys1, type="l", xlab="", ylab="")
lines(xs, ys2, lty=2)
lines(xs, ys3, lty=3)

text(c(0, 1, 7), c(.35, .2, .1), 
     c(
       expression(chi^2(2)),
       expression(chi^2(3)),
       expression(chi^2(5))))


# eg7. t分布 -- 标准化过程中没有使用总体的标准差sigma, 而是使用了样本中的标准差s
xs = seq(-4, 4, l=1000)
ys1 = dnorm(xs)
ys2 = dt(xs, 1)

par(mfrow=c(1,1))
plot(xs, ys1, type="l", xlab="", ylab="")
lines(xs, ys2, lty=2)
