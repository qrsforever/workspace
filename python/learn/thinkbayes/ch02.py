#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
贝叶斯定理(根据数据集D的变化更新H假设):

p(H|D) = p(H)p(D|H) / p(D)

p(H): 先验概率, 得到新数据前某个假设的概率
p(H|D): 后验概率, 看到新数据后, 我们计算该假设的概率
p(D|H): 似然度, 在假设下得到该数据的概率
p(D): 标准化常量, 在任何假设下得到这一数据的概率
"""

from thinkbayes import Pmf
from thinkbayes import Suite

def CH2_2():
    """
    Cookie Problem (曲奇饼问题)
    碗1: 30个香草味 10个巧克力味
    碗2: 20个香草味 20个巧克力味

          |     碗1       |     碗2       |
          | 香草 | 巧克力 | 香草 | 巧克力 |
   -------+---------------+---------------+
    先验  |     0.5       |     0.5       |
    ------+---------------+---------------+ 
    似然度| 0.75 | 0.25   |  0.5 | 0.5    | 
    ------+------+--------+---------------- 
    后验  |0.375 | 0.125  | 0.25 | 0.25   |
   -------+--^---+--------+----------^----+
          |  |   |        |          |    |
          |  +---+--------+----------+    |
    归一化| 0.6  |        |               |

      0.375 / (0.375 + 0.25)
    """                    

    # 先验
    pmf = Pmf()
    pmf.Set(x='b1', y=0.5)
    pmf.Set(x='b2', y=0.5)

    # 乘以似然度 (香草)
    pmf.Mult('b1', 0.75)
    pmf.Mult('b2', 0.5)

    # 归一化
    pmf.Normalize(fraction=1.0)
    print("b1 = %.3f" % (pmf.Prob('b1', default=0)))
    print("b2 = %.3f" % (pmf.Prob('b2', default=0)))

    class Cookie(Pmf):
        # 似然度
        mixes = { 
                'bow1': { 'vanilla': 0.75, 'chocolate': 0.24 },
                'bow2': { 'vanilla': 0.5,  'chocolate': 0.5  }
                }

        def __init__(self, hypos):
            Pmf.__init__(self)
            # 先验概率
            for hypo in  hypos:
                self.Set(hypo, 1)
            self.Normalize()

        # 计算后验概率
        def Update(self, data):
            for hypo in self.Values():
                # 在该假设的条件下, 计算似然度
                like = self.Likelihood(data, hypo)
                self.Mult(hypo, like)
            return self.Normalize()

        def Likelihood(self, data, hypo):
            mix = self.mixes[hypo]
            return mix[data]

    hypos = ["bow1", "bow2"]
    data = 'vanilla'
    cookie = Cookie(hypos)
    # D: 香草
    cookie.Update(data)
    for hypo, prob in sorted(cookie.Items()):
        print('p(%s/%s) = %.3f' % (hypo, data, prob))

    # 有放回replace, 取三块
    cookie = Cookie(hypos)
    dataset = ['vanilla', 'chocolate', 'vanilla']
    for data in dataset:
        cookie.Update(data)
    for hypo, prob in sorted(cookie.Items()):
        print('p(%s/%s) = %.3f' % (hypo, dataset, prob))

def CH2_4():
    """
    Monty Hall (蒙蒂大厅难题)

    D: 用户选择了A门后, 蒙蒂打开了B门(没有车在B后面)

          | 先验概率p(H)   |   似然度p(D|H)  |  p(H)p(D|H)  |  后验概率p(H|D)
    ------+----------------+-----------------+--------------+---------------- 
    假设A |      1/3       |      1/2        |     1/6      |      1/3        
    ------+----------------+-----------------+--------------+---------------- 
    假设B |      1/3       |       0         |      0       |       0         
    ------+----------------+-----------------+--------------+----------------  
    假设C |      1/3       |       1         |     1/3      |      2/3        
    ------+----------------+-----------------+--------------+----------------
                             (A门已被用户打开)
    """

    class MontyHall(Pmf):

        def __init__(self, hypos):
            Pmf.__init__(self)
            for hypo in hypos:
                self.Set(hypo, 1)
            self.Normalize()

        def Update(self, data):
            for hypo in self.Values():
                like = self.Likelihood(data, hypo)
                self.Mult(hypo, like)
            return self.Normalize()

        # H: A,B,C假设有车的门
        # D: 打开的门, 且没有车
        def Likelihood(self, data, hypo):
            if hypo == 'A':
                return 0.5
            if hypo == 'C':
                return 1
            return 0

    hypos = 'ABC'
    data = 'B'
    monty = MontyHall(hypos)
    monty.Update('B')
    for hypo, prob in sorted(monty.Items()):
        print('p(%s/%s) = %.3f' % (hypo, data, prob))


def CH2_5():
    """
    贝叶斯的Suite框架
    """
    class Cookie(Suite):
        mixes = { 
                'bow1': { 'vanilla': 0.75, 'chocolate': 0.24 },
                'bow2': { 'vanilla': 0.5,  'chocolate': 0.5  }
                }
        def Likelihood(self, data, hypo):
            mix = self.mixes[hypo]
            return mix[data]

    hypos = ["bow1", "bow2"]
    data = 'vanilla'
    cookie = Cookie(hypos)
    cookie.Update(data)
    cookie.Print()

    # 再次有放回取两块饼
    cookie.Update('chocolate')
    cookie.Update('vanilla')
    cookie.Print()

    class MontyHall(Suite):
        def Likelihood(self, data, hypo):
            if hypo == 'A':
                return 0.5
            if hypo == 'C':
                return 1
            return 0
        
    hypos = 'ABC'
    data = 'B'
    monty = MontyHall(hypos)
    monty.Update('B')
    monty.Print()


def CH2_6():
    """
    M&M豆问题
           Brown   Yellow   Red    Green   Orange   Tan  Blue
    1994 :  30%     20%     20%     10%     10%     10%   0%
    1996 :  13%     14%     13%     20%     16%     0%   24%
    -----------------------------------------------------------        

    假设A: 黄色来自1994袋子, 绿色来自1996
    假设B: 黄色来自1996袋子, 绿色来自1994
    (从一个袋子取一个黄色, 另一个袋子取绿色是独立事件)

                                                     
         先验概率p(H) |         似然度p(D|H)        | p(H)p(D|H)  |   后验概率   |
    ------------------+-----------------------------+-------------+--------------+
                      |  1994(Yellow)   1996(Green) |             |              |
    假设A      1/2    |           20  *  20         |   200       |    20/27     |
    bag1              |                             |             |              |
                      |  1996(Yellow)   1994(Green) |             |              |
    假设B      1/2    |           14  *  10         |   70        |    7/27      |
    bag2              |                             |             |              |
    ------------------+-----------------------------+-------------+--------------+
    """

    class M_And_M(Suite):
        mix94 = dict(brown=30, yellow=20, red=20, green=10, orange=10, tan=10)
        mix96 = dict(brown=13, yellow=14, red=13, green=20, orange=16, blue=24)
        hypoA = dict(bag1=mix94, bag2=mix96)
        hypoB = dict(bag1=mix96, bag2=mix94)
        hypos = dict(A=hypoA, B=hypoB)

        def Likelihood(self, data, hypo):
            bag, color = data
            mix = self.hypos[hypo][bag]
            return mix[color]

    suite = M_And_M('AB')
    suite.Update(('bag1', 'yellow'))
    suite.Update(('bag2', 'green'))
    suite.Print()


def CH2_8():
    """
    曲奇饼被吃掉
    """
    class Bowl():
        d = {}
        def __init__(self, d):
            self.d = d

        def eat(self, name, count):
            n = self.d[name]
            if n > count:
                n = n - count
            self.d[name] = n

        def likelihood(self, name):
            s = 0
            for c in self.d.values():
                s += c
            n = self.d[name]
            return float(n/s)


    class Cookie(Suite):
        mixes = {
                'bowl1': Bowl(dict(vanilla=30, chocolate=10)),
                'bowl2': Bowl(dict(vanilla=20, chocolate=20))
                }

        def Eat(self, hypo, piecename, count = 1):
            self.mixes[hypo].eat(piecename, count)
            
        def Likelihood(self, data, hypo):
            return self.mixes[hypo].likelihood(data)

    cookie = Cookie(['bowl1', 'bowl2'])
    cookie.Update('vanilla')
    cookie.Eat('bowl1', 'vanilla', count = 1)
    cookie.Update('chocolate')
    cookie.Eat('bowl1', 'chocolate', count = 1)
    cookie.Update('vanilla')
    cookie.Print()

if __name__ == "__main__": 
    CH2_2()
    print("-------------- ")
    CH2_4()
    print("-------------- ")
    CH2_5()
    print("-------------- ")
    CH2_6()
    print("-------------- ")
    CH2_8()
