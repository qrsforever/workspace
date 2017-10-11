#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import thinkstats

criteria = 10

def matches(counts, members, shoots, hitratio):
    """
    counts: 比赛场次数量
    members: 球员人数
    shoots: 投篮次数
    hitratio: 每个球员的投篮命中率
    """
    def match():
        """
        单场比赛
        """
        for m in range(members):
            successive = 0
            for s in range(shoots):
                hit = (random.random() >= (1 - hitratio))
                if hit:
                    successive += 1
                    if successive == criteria:
                        return 1
                else:
                    successive = 0
        return 0

    for c in range(counts):
        # 如果某单场比赛已经连续10投中退出
        if match():
            return 1  

    return 0

def main():
    simcount = 1000 # 模拟次数
    counts = [1, 82]  # 比赛场次1次和82次两种
    for m in counts:
        results = [matches(m, 10, 15, 0.5) for i in range(simcount)]    
        mu = thinkstats.Mean(results)
        print("matches %2d: prob = %.3f%% " % (m, mu * 100))

def match(criteria, matches=1):
    member = 10 
    k, p = 15*matches, 0.5

    for m in range(member):
        successive = 0
        for i in range(k):
            shoot = (random.random() >= (1-p))
            if shoot:
                successive += 1
                if successive == criteria:
                    return 1
            else:
                successive = 0
    return 0		

def main2():
    n = 1000
    criteria = 10
    matches = [1,82]
    results, prob = [], []
    for m in matches:
        results = [match(criteria,m) for i in range(n)]
        prob = thinkstats.Mean(results) * 100
        print('matches %2d: prob = %.3f%%' % (m, prob))

if __name__ == "__main__":
    main()
    print("-------------- ")
    main2()
