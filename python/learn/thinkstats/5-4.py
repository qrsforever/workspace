#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import thinkstats

def process():
    doors = ['A', 'B', 'C']
    # 指定一扇正确的门
    correct = random.choice(doors)
    # 选手选择一扇门
    select = random.choice(doors)
    # 删除选手选择的门
    doors.remove(select)

    # 主持人从剩余的门中打开一扇错误的门
    while True:
        s = random.choice(doors)
        # 跳过正确的门
        if s == correct: continue
        # 打开此门(错误的门)
        doors.remove(s)
        break

    # 重新选择的机会
    change_select = random.choice(doors)
    return select == correct, change_select == correct

def main():
    unchange_rate, change_rate = [], []  
    for i in range(1000):
        unchange, change = process()
        unchange_rate.append(unchange)
        change_rate.append(change)
    
    print("Mean(Unchange) = %.3f \t Mean(Change) = %.3f" % (thinkstats.Mean(unchange_rate), thinkstats.Mean(change_rate)))


if __name__ == "__main__":
    main()
