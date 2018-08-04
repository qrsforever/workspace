#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('res/chapter3/demo/data/catering_sale.xls', index_col = u'日期', sheet_name=0)
#  print(type(data))
#  print(len(data))
#  print(data.describe())

plt.figure()

pb = data.boxplot(return_type='dict')
#  plt.boxplot(x = data)
#  plt.boxplot(x = data, whis=1.5, patch_artist = True, showmeans = True,
   #  boxprops = {'color':'black','facecolor':'#9999ff'},
   #  flierprops = {'marker':'o','markerfacecolor':'red','color':'black'},
   #  meanprops = {'marker':'D','markerfacecolor':'indianred'},
   #  medianprops = {'linestyle':'--','color':'orange'}
   #  )

x = pb['fliers'][0].get_xdata()
#  print(x)
y = pb['fliers'][0].get_ydata()
#  print(y)
y.sort()

for i in range(len(y)):
    if i > 0:
        print("[%d %d]" % (x[i], y[i]))
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i]+0.05-0.8/(y[i]-y[i-1]), y[i]))
    else:
        print("[%d %d]" % (x[i], y[i]))
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i]+0.08, y[i]))

plt.show()
