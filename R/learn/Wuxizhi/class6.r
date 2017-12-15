#!/usr/bin/env Rscript

# eg.1 假设检验
w = scan("res/sugar.txt")

par(mfrow=c(1,1))
hist(x=w, main="Histogram of sugar weight")

summary(object = w)

# QQ正态图
par(mfrow=c(1,1))
qqnorm(w)
qqline(w)

# H0: u = 500 <=>  H1: u < 500
# 检验统计量的分布从H0导出, 如果有矛盾, 就对H0不利
# p值: 检验统计量取实现值以及更极端值的概率
# p值很小: 在H0下, 小概率的事件发生了
# 显著性水平alpha, PV < alpha 拒绝H0
# R软件给出PValue值, 一般不给alpha, PValue又叫观测的显著性水平(sig)
# alpha不是越小越好, 越小越不好拒绝H0, 导致犯第二类错误
# 显著性水平和临界值是前计算机时代, 因为计算难度
# 现在计算机直接给出P-Value和统计量的实现值

# Nvim: \rp可以直接看结果
result = t.test(x = w, mu = 500, alternative = "less")
print(result$p.value)


# eg.2 
w = scan("res/exh.txt")
result = t.test(w, mu = 20, alternative = "greater")
print(result$p.value)


# eg.3  (w1, w2必需相互独立)
w = read.table(file = "res/drug.txt", header = T)
w1 = w[w[,2]==1,1]
w2 = w[w[,2]==2,1]
t.test(w1, w2, alt="greater")


# eg.4 (w1, w2 并不相互独立, 不能是u1 = u2假设, 但是可以udiff = before - after的差后的数据)
w = read.table(file = "res/diet.txt", header = T)
w1 = w$before
w2 = w$after
summary(w1)
summary(w2)
# 我们是在H0的分布下做假设, 然后把实测数据扔进去, 发现这种假设下实测数据的概率很低
t.test(w$before - w$after, alt = "greater")
# or
t.test(w$before , w$after, alt = "greater", pair = T)

# eg.5: 总体比例的检验
# 电视收视率调查1500人, 某电视台期望25%看, 实测23%, 是否显著 
# 二项分布
# 方法一: 假设分布是B(1500, 0.25), 那么1500*0.23看此台的概率 ---> P-Value
# p-value: 0.03836
pbinom(q = 1500*0.23, size = 1500, prob = 0.25)

# 方法二: R精确检验 
# p-value: 0.03837
binom.test(0.23*1500, 1500, 0.25, alt="less")

# 方法三: 近似(样本量大), 历史计算问题, 被淘汰
# p-value: 0.3929
prop.test(0.23*1500, 1500, 0.25, alt="less")

# eg.5: 两个总体比例之差
# A收视率: 20%  B收视率: 21%   A比B好吗?
n1 = 1200
n2 = 1300

# 精确
binom.test(c(0.20*n1, 0.21*n2), c(n1, n2), alt="less")$p.value
# 近似
prop.test(c(0.20*n1, 0.21*n2), c(n1, n2), alt="less")$p.value


# eg.6: 连续型变量检验
data = scan("res/life.txt")
# 大于2的数据
data[data > 2]
# Question: 小于2的是否少于70% ?
# 把疑问作为H0: p = 0.7 (p <= 0.7, 等于0.7, p-value已经很小了, 小于0.7更是如此)
binom.test(x = sum(data < 2),
           n = length(data),
           p = 0.7,
           alternative = "greater")$p.value

# eg.7: 非参数检验(秩)
# 如果把数据排序, 中位数100, 大于100, 小于100各0.5的概率
# 实际上从样本上观测大于100的个数没有一半
data = scan("res/GS.TXT")
pbinom(q = 1000, size = 2000, prob = 0.5)
pbinom(q = sum(data > 100), size = length(data), prob = 0.5)

