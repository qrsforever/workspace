#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
sys.path.append("../thinkstats")
import correlation

def readFile(filename):
    """
    解析文件: 列名, 行名, 及数据
    """
    colnames = []
    rownames = []
    data = []
    for i, line in enumerate(open(filename)):
        fields = line.split('\t')
        if i == 0:
            colnames = fields[1:]
        else:
            rownames.append(fields[0])
            data.append([float(item) for item in fields[1:]])
    return colnames, rownames, data

def peasson_for_distance(xs, ys):
    # 计算皮尔逊相关系数, 返回1-r, 越相近距离越短 
    r = correlation.Corr(xs, ys)
    return 1-r

class bicluster(object):
    """
    一个cluster节点, 可以使叶子节点, 也可以是茎节点
    """
    def __init__(self, vec, id = None, left = None, right = None, distance = 0.0):
        self.vec = vec
        self.id = id
        self.left = left
        self.right = right
        self.distance = distance

def hcluster(rows, caculate_distance = peasson_for_distance):
    """
    (hierachical clustering)
    构建决策树 (分级聚类)
    """
    # 初始化, 每一行定义为一个叶子节点
    clusters = [bicluster(vec, i) for i, vec in enumerate(rows)]

    auto_dec_id = -1
    caches = {}

    # 两两合并茎节点, 直到只剩下一下
    while len(clusters) > 1:
        closest = 1.0
        closestpairs = (0, 1)
        nums = len(clusters)
        for i in range(nums):
            for j in range(i+1, nums):
                if (clusters[i].id, clusters[j].id) not in caches:
                    d = caculate_distance(clusters[i].vec, clusters[j].vec)
                    caches[(clusters[i].id, clusters[j].id)] = d

                if d < closest:
                    closest = d
                    closestpairs = (i, j)

        # 本轮找到最新节点对, 组合成新的cluster(取平均值)
        xcluster = clusters[closestpairs[0]]
        ycluster = clusters[closestpairs[1]]
        vec = [(x + y) / 2 for x, y in zip(xcluster.vec, ycluster.vec)] 
        newcluster = bicluster(vec, auto_dec_id, xcluster, ycluster, closest)
                
        # 更新决策树
        del clusters[closestpairs[1]]
        del clusters[closestpairs[0]]
        clusters.append(newcluster)

        # 更新ID
        auto_dec_id -= 1
    
    return clusters[0]

def print_clusters(cluster, labelnames = None, n = 0):
    print(" "*n, end='')
    if cluster.id < 0:
        print("-", cluster.distance)
    else:
        if labelnames == None: print(cluster.id)
        else: print(labelnames[cluster.id])
    
    if cluster.left != None: print_clusters(cluster.left, labelnames, n = n + 1)
    if cluster.right != None: print_clusters(cluster.right, labelnames, n = n + 1)

def main():
    """
           word1 wrod2 word3
    blog1                
    blog2    
    blog3

    """
    colnames, rownames, data = readFile("./res/blogdata.txt")
    root_cluster = hcluster(data)
    print_clusters(root_cluster, rownames)


if __name__ == "__main__":
    main()
