#!/usr/bin/env Rscript

############################################################
### 奇异矩阵(不可逆)
### 非奇异矩阵
############################################################

A = cbind(c(3,5), c(4,6))
## |A| 不为0 --> A可逆
det(A)