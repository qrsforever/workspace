#!/usr/bin/env Rscript

v = read.table("res/Billianaires.TXT", sep=",", header=T, na.strings="-") 
w = v[v[,6]=="United States"|v[,6]=="China"|v[,6]=="Japan",]
w[,6] = as.character(w[,6])

# eg.1 位置统计量(location statistic)
w1 = w[w[,6]=="China", ]
w2 = w[w[,6]=="United States", ]
w3 = w[w[,6]=="Japan", ]

mean(w1$Age, na.rm=T)
mean(w2$Age, na.rm=T)
mean(w3$Age, na.rm=T)

median(w1$Age, na.rm=T)
median(w2$Age, na.rm=T)
median(w3$Age, na.rm=T)

quantile(v$Age, .25, na.rm=T)
quantile(v$Age, .75, na.rm=T)

# 众数mode (样本中出现的条目最多的)
z = table(v$Age)
modeAge = max(z)
z[which(z == modeAge)]

# which.min(w1$Age)

# eg.2 尺度统计量(scale statistic)
# 极差(Range)
paste("China Age range: ", 
      max(w1$Age), " - ", 
      min(w1$Age), " = ", 
      max(w1$Age) - min(w1$Age))
print(diff(range(w1$Age)))

paste("United States Age range: ", 
      max(w2$Age), " - ", 
      min(w2$Age), " = ", 
      max(w2$Age) - min(w2$Age))
print(diff(range(w2$Age)))

paste("Japan Age range: ", 
      max(w3$Age), " - ", 
      min(w3$Age), " = ", 
      max(w3$Age) - min(w3$Age))
print(diff(range(w3$Age)))

# 四分位间距/极差 (interquantile range) 
paste("China Age interquantile  range: ", 
      quantile(w1$Age, .75), " - ", 
      quantile(w1$Age, .25), " = ", 
      quantile(w1$Age, .75) - quantile(w1$Age, .25))
print(diff(quantile(w1$Age, c(.25, .75))))

paste("United States Age interquantile range: ", 
      quantile(w2$Age, .75), " - ", 
      quantile(w2$Age, .25), " = ", 
      quantile(w2$Age, .75) - quantile(w2$Age, .25))
print(diff(quantile(w2$Age, c(.25, .75))))

paste("Japan Age interquantile range: ", 
      quantile(w3$Age, .75), " - ", 
      quantile(w3$Age, .25), " = ", 
      quantile(w3$Age, .75) - quantile(w3$Age, .25))
print(diff(quantile(w3$Age, c(.25, .75))))

# 方差, 标准差, 标准得分 
paste("sd(w1), var(w1): ", sd(w1$Age), var(w1$Age))
paste("sd(w2), var(w2): ", sd(w2$Age), var(w2$Age))
paste("sd(w3), var(w3): ", sd(w3$Age), var(w3$Age))
print(scale(w1))
