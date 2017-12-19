#!/usr/bin/env Rscript



#### matrix

### 4x6 全填1
X = matrix(1, 4, 6)

rownames(X) = paste("S", seq(1, dim(X)[1]), sep = "")
colnames(X) = paste("V", seq(1, dim(X)[2]), sep = "")

### outer product
a = 1:3
b = 1:5
ab1 = a %o% b
ab2 = outer(a, b, "*")
## ?? ab3 == ab1 == ab2
ab3 = a %*% t(b)

## 真正理解一下outer函数作用
f = function(x, y) x + y
ab4 = outer(a, b, f)
