#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math

def cacShannonEntropy(dataSet):# {{{
    """
    计算香浓熵(信息熵)

    Parameters:
    ----------------
    dataSet: 最后一列为标签类别
                混合的分类越多, 熵越大
    Returns:
    ----------------
    shannonEnt: 信息期望

    """
    dataLen = len(dataSet)
    groups = { }
    for row in dataSet:
        label = row[-1]
        groups[label] = groups.get(label, 0) + 1

    shannonEnt = 0.0
    for label, count in groups.items():
        prob = count / dataLen
        # 信息: -math.log(prob, 2), 再*prob就是信息期望
        shannonEnt += -math.log(prob, 2) * prob

    return shannonEnt
# }}}

def createDataSet():# {{{
    """
    生成测试数据
    """
    arr = [
            [1, 2, 'A'],
            [3, 4, 'B'],
            [1, 3, 'E'],
            [3, 6, 'C'],
            [5, 7, 'D'],
            [4, 9, 'B'],
            [4, 3, 'D'],
            [8, 1, 'A']]

    return arr
# }}}

def main():
    dataSet = createDataSet()
    H = cacShannonEntropy(dataSet)
    print(H)

    print("End")

if __name__ == "__main__":
    main()
