## 汇总统计

### 离散

1. 频数
2. 众数: 频数最大的

### 连续,位置度量

1. 均值
2. 最大值, 最小值
3. 中值

### 离散度

1. 极差值: Max(data) - Min(data), 四分位数极差IRQ
2. 方差: 由均值算出, 均值受离群点影响, 所以方差也会有影响
3. AAD, MAD, IRQ
   AAD: absolute average deviation 绝对平均偏差
   MAD: median absolute deviation 中位数绝对偏差
   IRQ: interquartile range 四分位数极差

### 多元属性

1. 协方差, 协方差矩阵的对角线是属性自身的方差
   covariance(xi, xi) = variance(xi)

2. 相关性, 协方差=0, 说明两属性之间没有相关性, 但是如果值不为零时,不能使用它作为评价属性间的相关程度, 只是因为属性的度量不一致, 应该使用相关性.
   corelation(xi, xj)

  *协方差用来判断是 正/负/无 相关*