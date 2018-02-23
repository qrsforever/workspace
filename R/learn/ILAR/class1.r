#!/usr/bin/env Rscript


a = c(1,2,3)
# 显示是column vector
print(a)

# 显示的是行向量 [, x] 
b = t(a)

7*a

# a列向量 b行向量, 为啥能相加
#     1 2 3 
#  1
#  2
#  3
c1 = a + b

# 列向量相加
c2 = t(b) + a

# 行向量相加 == c1
c3 = b + t(a)

a = c(1,3,2)
a
b = c(2,8,9)
b
a + b
# 这个不是内积, 只是相乘
a*b
# 做求和运算(内积)
sum(a*b)

# 向量的length
sqrt(sum(a*a))

# 0-vector
rep(0, 5)

# 1-vector
rep(1, 3)

# (1,3) (2,2), (8,9) col by col
a = c(1,3)
b = c(2,2)
c = c(8,9)
A = matrix(c(a, b, c), ncol = 3)
A
A = matrix(c(a, b, c), ncol =3, byrow=T)
A

A1 = rbind(c(1, 3, 2), c(2, 8, 9))
A1

7*A1
t(A1)

B = matrix(c(5,8,3,4,2,7),ncol=3,byrow=T)
B
A+B

# A: 2x3  a:3x1
a = c(1, 3, 2)
# 注意形式: Aa
print(A)
print(A%*%a)
# ?????
print(A*a)
