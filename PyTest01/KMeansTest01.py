#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/6/15 0015 下午 4:19
# @Author: XieHaoHao
# @File  : KMeansTest01.py
# KMeans算法的使用

import numpy as np
from sklearn.cluster import KMeans

if __name__ == '__main__':

    def loadData(filePath):
        fr = open(filePath,'r+',encoding='utf-8-sig')   #指定编码方式为“utf-8-sig”
        lines = fr.readlines()
        retData = []
        retCityName = []
        for line in lines:
            items = line.strip().split(",")
            retCityName.append(items[0])
            retData.append([float(items[i]) for i in range(1,len(items))])
        return retData,retCityName

    data,cityName = loadData('Data\\provinceData.txt')
    print(cityName)
    for da in data:
        print(da)
    km = KMeans(n_clusters=3)
    label = km.fit_predict(data)
    expenses = np.sum(km.cluster_centers_,axis=1)
    print('--------------------------------------')
    print(label)
    print(expenses)
    print('result-result-result-result-result-result-result-result')
    CityResult = [[],[],[]]
    for i in range(len(cityName)):
        CityResult[label[i]].append(cityName[i])
    for i in range(len(CityResult)):
        print("expenses = %.2f" % expenses[i])
        print(CityResult[i])


