#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/6/16 0016 下午 7:28
# @Author: XieHaoHao
# @File  : ClassificationTest02.py

"""
SVM支持向量机
"""

import pandas as pd
import numpy as np
from sklearn import svm
from sklearn import model_selection

# 引入交叉验证
from sklearn.model_selection import cross_validate

# parse_dates：指的是将那一列作为时间列，可以是多列，如parse_dates=[0, 1]
# index_col：指的是将那一列作为序号列
data = pd.read_csv('Data/equity.csv', encoding='utf-8-sig', parse_dates=[0], index_col=0)

# 按时间进行升序排列
data.sort_index(0, ascending=True, inplace=True)

dayfeature = 10
featurenum = 5 * dayfeature

# np.zeros()为创建值为0数组
x = np.zeros((data.shape[0] - dayfeature, featurenum + 1))      # 记录10天的51个特征值，其中最后一个特征是
y = np.zeros((data.shape[0] - dayfeature))                      # 记录涨跌

for i in range(0, data.shape[0] - dayfeature):
    x[i, 0:featurenum] = np.array(data[i:i + dayfeature]
                                      [[u'收盘价', u'最高价', u'最低价', u'开盘价', u'成交量']]).reshape((1, featurenum))
    x[i, featurenum] = data.ix[i + dayfeature][u'开盘价']

for i in range(0, data.shape[0] - dayfeature):
    # data.ix：ix指的是使用行标签进行寻找
    if data.ix[i + dayfeature][u'收盘价'] >= data.ix[i + dayfeature][u'开盘价']:
        y[i] = 1
    else:
        y[i] = 0

clf = svm.SVC(kernel='rbf')
result = []
for i in range(5):
    x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2)
    clf.fit(x_train, y_train)
    result.append(np.mean(y_test == clf.predict(x_test)))
print("svm classifier accuacy:")
print(result)