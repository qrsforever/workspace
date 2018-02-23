#!/usr/bin/env Rscript

# file: grade class standardized
w = read.table("res/grade.txt", header=T)
par(mfrow=c(1,3))

c1 = w[w$class ==1, ]
c2 = w[w$class ==2, ]

m1 = mean(c1$grade)
m2 = mean(c2$grade)

s1 = sqrt(var(c1$grade))
s2 = sqrt(var(c2$grade))

# round: 控制精度, stand1, stand2 应该和文件中一样
stand1 = round((c1$grade - m1) / s1, 2)
stand2 = round((c2$grade - m2) / s2, 2)

# nrow <---> summary(stand1 == c1$standardized)[2]
nr1 = nrow(c1)
nr2 = nrow(c2)
summary(stand1 == c1$standardized)[2]
summary(stand2 == c2$standardized)[2]

boxplot(grade~class, w, main="Original Grades")
boxplot(standardized~class, w, main="Standardized Grades")
boxplot(standardized~class, rbind(c1, c2), main="My-Standardized Grades")
