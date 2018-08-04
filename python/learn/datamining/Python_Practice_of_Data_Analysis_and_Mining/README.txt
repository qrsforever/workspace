资源下载(res):
    https://pan.baidu.com/s/12WFBgZ4F0lq4Nd8CAOK87Q
官网:
    http://www.tipdm.org/bdrace/index.html



Box
===

```
plt.boxplot(x, notch=None, sym=None, vert=None, 
            whis=None, positions=None, widths=None, 
            patch_artist=None, meanline=None, showmeans=None, 
            showcaps=None, showbox=None, showfliers=None, 
            boxprops=None, labels=None, flierprops=None, 
            medianprops=None, meanprops=None, 
            capprops=None, whiskerprops=None)

x：指定要绘制箱线图的数据；
notch：是否是凹口的形式展现箱线图，默认非凹口；
sym：指定异常点的形状，默认为+号显示；
vert：是否需要将箱线图垂直摆放，默认垂直摆放；
whis：指定上下须与上下四分位的距离，默认为1.5倍的四分位差；
positions：指定箱线图的位置，默认为[0,1,2…]；
widths：指定箱线图的宽度，默认为0.5；
patch_artist：是否填充箱体的颜色；
meanline：是否用线的形式表示均值，默认用点来表示；
showmeans：是否显示均值，默认不显示；
showcaps：是否显示箱线图顶端和末端的两条线，默认显示；
showbox：是否显示箱线图的箱体，默认显示；
showfliers：是否显示异常值，默认显示；
boxprops：设置箱体的属性，如边框色，填充色等；
labels：为箱线图添加标签，类似于图例的作用；
filerprops：设置异常值的属性，如异常点的形状、大小、填充色等；
medianprops：设置中位数的属性，如线的类型、粗细等；
meanprops：设置均值的属性，如点的大小、颜色等；
capprops：设置箱线图顶端和末端线条的属性，如颜色、粗细等；
whiskerprops：设置须的属性，如颜色、粗细、线的类型等；

```

http://www.bubuko.com/infodetail-1120930.html

matplotlib中boxplot常用的术语:

whiskers, 是指从box 到error bar之间的竖线
fliers, 是指error bar线之外的离散点. 维基上的叫法是 Outliers
caps, 是指error bar横线
boxes, Q1 和 Q3组成的box, 即25分位和75分位.
medians, 是中位值的横线.
means, 是avg的横线.

boxplot() 函数参数:

参数x: data的输入, 格式是: 由vector组成的一个list

参数whis: 用来确定 error bar的位置,  上面的那条error bar的位置等于: Q3 + whis*IQR, 下面的那条error bar的位置等于 Q1-whis*IQR,
    其中IQR = interquartile range 即 Q3-Q1, whis缺省值为1.5.

boxplot() 函数还可针对箱线图上每个绘图元素指定的绘图风格, 这些参数有: boxprops,flierprops, medianprops, meanprops,capprops,
    whiskerprops属性. 每个绘图风格属性都是dict对象, 下面是一个比较完整属性设定,
    dict(linestyle=‘solid‘, color=‘blue‘, linewidth=1, marker=‘o‘, markerfacecolor=‘red‘, markeredgecolor=‘black‘, markeredgewidth=3, markersize=12)

返回对象:

bp作为boxplot()返回对象.
bp.bxpstats属性包含下面几个子属性.
    med属性: 中位值.
    q1: box的下边界, 即25分位值.
    q3: box的上边界, 即75分位值.
    whislo: 下面的那条error bar值.
    whishi: 上面的那条error bar值.
bp的其他重要属性还有:
    boxes, 是25分位值和75分位值构成的box, 每个box是一个Line2D对象, 注意是Line2D对象
    medians, 是中位值的横线, 每个median是一个Line2D对象
    whiskers, 是指从box 到error bar之间的竖线. 每个whisker是一个Line2D对象
    fliers, 是指error bar线之外的离散点. 每个flier是一个Line2D对象
    caps, 是指error bar横线. 每个cap是一个Line2D对象
    means, 是avg的横线, 每个mean是一个Line2D对象
一旦能访问到这些Line2D对象, 就可以做更多的定制化了, 比如设置线性/颜色等, 因为有了位置信息, 甚至可以派生出其他Line2D对象.
