#!/usr/bin/env Rscript

## 加载文件的数据
source("./factor_levels.r")
state
statef

incomes = c(60, 49, 40, 61, 64, 60, 59, 54, 62, 69, 70, 42, 56,
61, 61, 61, 58, 51, 48, 65, 49, 49, 41, 48, 52, 46,
59, 46, 58, 43)

## 应用一个函数在某个因素各水平上
incmeans = tapply(X = incomes, INDEX = statef, FUN = mean)
round(incmeans, 2)

stderr = function(x) sqrt(var(x)/length(x))

incstderr = tapply(incomes, statef, stderr)
round(incstderr, 2)
