#!/usr/bin/env Rscript

#### matrix

############################################################
### Arrays
############################################################
z = 1:24
dim(z) = c(3, 4, 2)

## all data
z[,,]
z[1,,]

x = array(1:20, dim = c(4,5))


### 4x6 全填1
X = matrix(1, 4, 6)

rownames(X) = paste("S", seq(1, dim(X)[1]), sep = "")
colnames(X) = paste("V", seq(1, dim(X)[2]), sep = "")

### outer product
a = 1:3
b = 1:5
### 外积的维度是由两个向量共同决定
ab1 = a %o% b
ab2 = outer(a, b, "*")
## ?? ab3 == ab1 == ab2
ab3 = a %*% t(b)

## 真正理解一下outer函数作用
f = function(x, y) x + y
ab4 = outer(a, b, f)

### 1到20, 矩阵以row下标跑的块(列元素是顺序的)
Y = matrix(1:20, 4, 5)
#      [,1] [,2] [,3] [,4] [,5]
# [1,]    1    5    9   13   17
# [2,]    2    6   10   14   18
# [3,]    3    7   11   15   19
# [4,]    4    8   12   16   20

### 方阵才有逆
A = c(c(0,1,4), c(1,0,-3), c(2,3,8))
dim(A) = c(3,3)
B = solve(A)
A %*% B
