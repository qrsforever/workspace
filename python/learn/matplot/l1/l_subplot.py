#!/usr/bin/python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt  
  
x1 = [1, 2, 3]
y1 = [3, 2, 1]
x2 = [2, 3, 4]
y2 = [3, 1, 2]

plt.figure(figsize=(10,8), dpi=98)
p1 = plt.subplot(2, 2, 1) # 2行2列 第一区域
p2 = plt.subplot(2, 2, 4) # 2行2列 第四区域

l1, = p1.plot(x1, y1, color='r', linewidth=4.5, linestyle="--", label="sample1")
#  p1.set_xticks( rotation='vertical')
p1.axis([0, 5, 0, 5])
p1.set_title("P1")
p1.set_xlabel("P1-X")
p1.set_ylabel("P1-Y")
p1.set_yticks(y1) # 必须是数字
p1.set_yticklabels(["$%.2f$" % y for y in y1]) # 上面yticks数字一一对应的label
p1.grid(True)
print(l1) # Line2D(sample1)
p1.legend(loc='upper right') # not using l1, so is "sample1"

l2, = p2.plot(x2, y2, color='b', linewidth=4.5, linestyle="-.", label="sample2")
p2.axis([0, 6, 0, 6])
#  p2.set_axes([0, 5, 0, 5]) # no usefull
p2.set_title("P2")
p2.set_xlabel("P2-X")
p2.set_ylabel("P2-Y")
p2.set_xticks(x2)
p2.set_xticklabels(['20170510', '20170511', '20170512'], rotation=30)
p2.grid(True)
p2.legend([l2], ['P2-L2'], loc='upper left')

plt.show()
