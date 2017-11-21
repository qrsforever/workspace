#!/usr/bin/python3
# -*- coding: utf-8 -*-

from math import sqrt

# A dictionary of movie critics and their ratings of a small
# set of movies
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
    'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
    'The Night Listener': 3.0},
    'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
        'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
        'You, Me and Dupree': 3.5},
    'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
        'Superman Returns': 3.5, 'The Night Listener': 4.0},
    'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
        'The Night Listener': 4.5, 'Superman Returns': 4.0,
        'You, Me and Dupree': 2.5},
    'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
        'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
        'You, Me and Dupree': 2.0},
    'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
        'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
    'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

def sim_distance(perfs, p1, p2):
    """
    欧几里得距离(Euclidean Distance Score)
    基于欧几里得距离-两人影评相似度                           
    返回: 0 - 1,  0: 完全不通风格, 1: 及其相似

    如果评级人水平有差别, 但是喜爱偏好相似就无法区分
    """
    shared_items = {}
    for item in perfs[p1]:
        if item in perfs[p2]:
            shared_items[item] = 1
            break
    if len(shared_items) == 0: return 0

    sum_of_squares = sum([pow(perfs[p1][item] - perfs[p2][item], 2) 
        for item in perfs[p1] if item in perfs[p2]])
    
    return 1/(1 + sqrt(sum_of_squares))

def sim_pearson(perfs, p1, p2):
    """
    皮尔逊相关系数(Pearson correlation coefficient)
    cov(X, Y) / sigmaX*sigmaY
    协方差(X,Y) / X的标准方差*Y的标准方差
    """
    shared_items = {}
    for item in perfs[p1]:
        if item in perfs[p2]:
            shared_items[item] = 1

    n = len(shared_items)

    if n == 0: return 0 

    # 计算影评均值
    mu_p1 = sum([perfs[p1][it] for it in shared_items]) / n
    mu_p2 = sum([perfs[p2][it] for it in shared_items]) / n
    print(mu_p1, mu_p2)

    # 计算标准方差
    sigma_p1 = sqrt(sum([pow(perfs[p1][it]-mu_p1, 2) for it in shared_items]))
    sigma_p2 = sqrt(sum([pow(perfs[p2][it]-mu_p2, 2) for it in shared_items]))
    print(sigma_p1, sigma_p2)

    # 计算协方差
    cov = sum([(perfs[p1][it]-mu_p1)*(perfs[p2][it]-mu_p2) for it in shared_items])
    print(cov)

    return cov / sigma_p1*sigma_p2

def CH2_1():
    print(sim_distance(critics, 'Lisa Rose', 'Gene Seymour'))
    print(sim_pearson(critics, 'Lisa Rose', 'Gene Seymour'))


if __name__ == "__main__":
    #  print(critics)
    CH2_1()
