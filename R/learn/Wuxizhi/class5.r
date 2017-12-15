#!/usr/bin/env Rscript

# eg.1 总体均值mu的区级估计
weight = scan("res/noodle.TXT")
summary(weight)
result = t.test(weight, con =.95)
print(result$con)

# eg.2 两个总体均值之差估计(mu1 - mu2)
v = read.table("res/expend.txt", header=T)
v1 = v[v[, 2] == 1, 1]
v2 = v[v[, 2] == 2, 1]

m1 = mean(v1)
m2 = mean(v2)

diff = m1 - m2
print(diff)

sd(v1)
sd(v2)

t.test(v1, con=.95)$con
t.test(v2, con=.95)$con

t.test(v1, v2, con=.90)$conf


