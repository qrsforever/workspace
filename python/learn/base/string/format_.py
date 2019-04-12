#!/usr/bin/python3
# -*- coding: utf-8 -*-

print('{1}:{0}'.format(2, 1))
# out: 1:2

# 精度控制
print('[{0:.3}]'.format(1/3))
# out: [0.333]

# 宽度控制
print('[{0:7}]'.format('hello'))
# out: [hello  ]

# <codecell>
# 居左
print('[{0:<7.3}]'.format(1/3))
# out: [0.333  ]

# <codecell>
# 居右
print('[{0:>7.3}]'.format(1/3))
# out: [  0.333]

# <codecell>
# 居中
print('[{0:^7.3}]'.format(1/3))
# out: [ 0.333 ]

# <codecell>
# 补全(左补0)
print('[{0:0>7}]'.format(1))
print('[{0:{1}>7}]'.format(1, 0))
# out: [0000001]

# <codecell>
# 补全(右补0)
print('[{0:0<7}]'.format(1))
print('[{0:{1}<7}]'.format(1, 0))
# out: [1000000]

# <codecell>
# 中文空格对齐
blog = {'1':'中国石油大学','2':'浙江大学','3':'南京航空航天大学'}
print('不对齐')
print('{0:^4}\t\t{1:^8}'.format('序号', '名称'))
for no, name in blog.items():
    print('{0:^4}\t\t{1:^8}'.format(no, name))

# out:
# 序号 		   名称   
# 1  		 中国石油大学 
# 2  		  浙江大学  
# 3  		南京航空航天大学

print('对齐')
print('{0:^4}\t\t{1:{2}^8}'.format('序号', '名称', chr(12288)))
for no, name in blog.items():
    print('{0:^4}\t\t{1:{2}^8}'.format(no, name, chr(12288)))

# out:
#  序号 		　　　名称　　　
#  1  		　中国石油大学　
#  2  		　　浙江大学　　
#  3  		南京航空航天大学
