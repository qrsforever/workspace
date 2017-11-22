#!/usr/bin/python3
# -*- coding: utf-8 -*-

from math import sqrt
import sys
sys.path.append("../thinkstats")
import correlation
import thinkplot

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

show = 0

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

    # p1, p2共同的影评数据
    data_p1 = [perfs[p1][it] for it in shared_items]
    data_p2 = [perfs[p2][it] for it in shared_items]

    # 计算影评均值
    mu_p1 = sum(data_p1) / n
    mu_p2 = sum(data_p2) / n
    #  print(mu_p1, mu_p2)

    # 计算标准方差
    var_p1 = sum([pow(it-mu_p1, 2) for it in data_p1]) / n
    var_p2 = sum([pow(it-mu_p2, 2) for it in data_p2]) / n
    #  print(var_p1, var_p2)

    if var_p1 == 0 or var_p2 == 0: return 0

    # 计算协方差
    cov = sum([(x-mu_p1)*(y-mu_p2) for x, y in zip(data_p1, data_p2)]) / n
    #  print(cov)

    # 计算皮尔逊相关系数
    r = cov / sqrt(var_p1*var_p2)

    # ============  thinkstat 方法 ===============

    if show:
        rr = correlation.Corr(data_p1, data_p2)
        print(r, rr)
        thinkplot.Clf()
        thinkplot.Scatter(data_p1, data_p2)
        thinkplot.Show()
    
    return r

def topMatch(perfs, person, n = -1, similarity = sim_pearson):
    """
    计算与person品味相关系数
    """
    scores = [(similarity(perfs, person, it), it) for it in perfs if it != person]
    scores.sort(key=None, reverse=True)
    return scores[0:n]

def getRecommendations(perfs, person, similarity = sim_pearson):
    """
    推荐person应该喜欢的电影
    """
    sum_info = {} # 对电影加权评分之和 + 相似度之和
    for other in perfs:
        # 排除自己
        if other == person: continue

        # 计算和这个人的相似度
        r = similarity(perfs, person, other)

        # 排除相似度不明显的
        if r <= 0: continue

        # 遍历这个人的所有影评
        for item in perfs[other]:
            # 如果看过这部电影, 就不需要推荐
            if item in perfs[person]: continue
            
            # 相似度 * 影评值 = 加权相似度
            score = perfs[other][item] * r

            # 记录每部影片的加权score之和, 及相似度之和
            sum_info.setdefault(item, [0.0, 0.0])
            sum_info[item][0] += score
            sum_info[item][1] += r

    #  print(sum_info)
    
    # 建立一个归一化list
    rankings = [(it, sum_info[it][0]/sum_info[it][1]) for it in sum_info]
    rankings.sort(key=lambda it: it[1], reverse=True)
    return rankings 

def transformPrefs(prefs):
    """
    {'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5},
     'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5}}
    to:
    {'Lady in the Water':{'Lisa Rose':2.5,'Gene Seymour':3.0},
     'Snakes on a Plane':{'Lisa Rose':3.5,'Gene Seymour':3.5}}
    """
    results = {}
    for person in prefs:
        for movie in prefs[person]:
            results.setdefault(movie, {})
            results[movie][person] = prefs[person][movie]
    return results

def calculateSimilarItems(prefs, n=10):
    results = {}
    itemPrefs = transformPrefs(prefs)
    for item in itemPrefs:
        scores = topMatch(itemPrefs, item, n, similarity = sim_distance)
        results[item] = scores
        print(item, scores)
    return results

def getRecommendedItems(prefs, itemMatch, user):
    userRatings=prefs[user]
    scores={}
    totalSim={}
    # Loop over items rated by this user
    for (item, rating) in userRatings.items( ):
        # Loop over items similar to this one
        for (similarity, item2) in itemMatch[item]:
            # Ignore if this user has already rated this item
            if item2 in userRatings: continue
            # Weighted sum of rating times similarity
            scores.setdefault(item2,0)
            scores[item2]+=similarity*rating
            # Sum of all the similarities
            totalSim.setdefault(item2,0)
            totalSim[item2]+=similarity

    # Divide each total score by total weighting to get an average
    rankings=[(score/totalSim[item],item) for item,score in scores.items( )]
    # Return the rankings from highest to lowest
    rankings.sort( )
    rankings.reverse( )
    return rankings

def loadMovieLens(path='res'):
    """
    解析数据 { "user" : {"movie1" : rating, ... } }
    """

    movies = {}
    # movieid | title | date
    for line in open(path + "/u.item", encoding="ISO-8859-1"):
        (id, title) = line.split('|')[0:2]
        movies[id] = title
 
    dataset = {}
    # user movieid rating ts
    for line in open(path + "/u.data"):
        (user, id, rating) = line.split("\t")[0:3]
        dataset.setdefault(user, {})
        dataset[user][movies[id]] = float(rating)

    return dataset

def CH2_1():
    print(sim_distance(critics, 'Lisa Rose', 'Gene Seymour'))
    print(sim_pearson(critics, 'Lisa Rose', 'Gene Seymour'))
    print(topMatch(critics, 'Toby', 3))
    print(getRecommendations(critics, 'Toby', similarity = sim_pearson))
    print(getRecommendations(critics, 'Toby', similarity = sim_distance))

def CH2_2():
    itemsim = calculateSimilarItems(critics)
    print(getRecommendedItems(critics, itemsim, 'Toby'))

def CH2_3():
    prefs = loadMovieLens()

    # User-Based
    print(getRecommendations(prefs, '87', similarity = sim_pearson)[0:30])

    # Item-Based
    itemsim = calculateSimilarItems(prefs,n=50)
    print(getRecommendedItems(prefs,itemsim,'87')[0:30])

if __name__ == "__main__":
    CH2_1()
    CH2_2()
    #  CH2_3()
