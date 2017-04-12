#!/usr/bin/python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt  
  
x1 = [0, 1, 2, 3, 4, 5, 6]
xx = ['Input', 'L.pause', 'S.new_inent', 'L.on_pause', 'S.resume', 'S.on_resume', 'S.Draw']
y1 = [0, 172, 180, 436, 504, 632, 936]

plt.figure()
#  plt.xlim(0.0, 7)
#  plt.ylim(0.0, 1500)
plt.axis([0.0, 7, 0.0, 1500]) # 与上面的等价
plt.plot(x1, y1, color='r', linewidth=4.5, linestyle="-", label="sample1")
plt.xticks(x1, xx, rotation='vertical')
plt.xlabel("EventStatus")
plt.ylabel("Time(ms)")
plt.title("Start Activity Time")
plt.grid(True)
plt.legend(loc='upper left')
plt.show()

# character	   description
#   '-'	        solid line style
#   '--'        dashed line style
#   '-.'        dash-dot line style
#   ':'	        dotted line style
#   '.'	        point marker
#   ','	        pixel marker
#   'o'	        circle marker
#   'v'	        triangle_down marker
#   '^'	        triangle_up marker
#   '<'	        triangle_left marker
#   '>'	        triangle_right marker
#   '1'	        tri_down marker
#   '2'	        tri_up marker
#   '3'	        tri_left marker
#   '4'	        tri_right marker
#   's'	        square marker
#   'p'	        pentagon marker
#   '*'	        star marker
#   'h'	        hexagon1 marker
#   'H'	        hexagon2 marker
#   '+'	        plus marker
#   'x'	        x marker
#   'D'	        diamond marker
#   'd'	        thin_diamond marker
#   '|'	        vline marker
#   '_'	        hline marker

# character	color
#   ‘b’	        blue
#   ‘g’	        green
#   ‘r’	        red
#   ‘c’	        cyan
#   ‘m’	        magenta
#   ‘y’	        yellow
#   ‘k’	        black
#   ‘w’	        white
