#!/usr/bin/env Rscript


### For data analysis, the typical data matrix is organized with
### rows containing the responses of a particular subject and the
### columns representing different variables.

data = matrix(seq(1:24), ncol = 4)
### dim() 返回维度list, S: subject, V: variable
### 行列标题名
rownames(data) = paste("S", seq(1, dim(data)[1]), sep = "")
colnames(data) = paste("V", seq(1, dim(data)[2]), sep = "")

### t()转置
t(data)


v = 1:4

### 结果不是期望的 ( 一列方向(columnwise)轮着加v)
data + v

### 这是我们需要的
t(t(data) + v)


### 偏差分数(deviation scores): 每个数减去列向量的均值(colMeans)
### scale = TRUE(The default for scale is to convert a matrix to standard scores)
scale(x = data, scale = FALSE)
scale(x = data, scale = TRUE)


### 矩阵相加
x = c(1, 2, 3, 4)
### 
x + x
### todo: 错误
# x %+% t(x)

### 标量 (内积)
### x %*% x = sum(x * x)
x %*% x
sum(x * x)

### 矩阵 (×乘: 外积)
x %*% t(x)

### 求colMeans, 可以使用one vector
# rownum = dim(data)[1]
one = rep(1, dim(data)[1])
t(one)

# data.mean = colMeans()
data.means = (t(one) %*% data) / dim(data)[1]
colMeans(data)

# 偏差分数(deviation scores): == scale
data.diff = data - one %*% data.means
data.cen = scale(data, scale=FALSE)


### 随机矩阵
set.seed(42)
## 从data里面的数据随机取
data1 = matrix(sample(data), ncol = 4)

### 协方差
data1.means = (t(one) %*% data1) / dim(data1)[1]
data1.diff = data1 - one %*% data1.means
data1.cov = (t(data1.diff) %*% data1.diff) / (dim(data1)[1] - 1)
### 下面两行 == 
round(data1.cov, 2)
round(cov(data1), 2)


diag(data1.cov)


#########
x = matrix(c(1,2,3,4), ncol=2)

### 每个元素对应位置上相乘(纯相乘, 没有加的操作)
###   1  2   1 3      1*1  2*3
###        *     --->   
###   3  4   2 4      3*2  4*4
t(x)*x

### 矩阵相乘%*%: 有乘的操作和加的操作
t(x)%*%x
### 交叉乘积（cross product）：crossprod(X，Y)等同于t(X) %*% y，crossprod(X)等价于crossprod(X, X)；
### == t(x)%*%x
crossprod(x)

### 外积: 把矩阵分成多个向量分别计算
x%o%x

### 
install.packages("LoopAnalyst")
library("LoopAnalyst")

make.adjoint(x)
