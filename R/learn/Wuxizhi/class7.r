#!/usr/bin/env Rscript

# SalaPreMBA SalaPostMBA Tuition GMAT
data = read.table(file = "res/bschool.txt", header = T)
par(mfrow=c(1,1))
# SalaPostMBA 和 SalaPreMBA 散点图
plot(SalaPostMBA~SalaPreMBA, data, pch=16)
