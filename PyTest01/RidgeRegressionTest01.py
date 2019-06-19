#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/6/17 0017 下午 8:15
# @Author: hao
# @File  : RidgeRegressionTest01.py
# 岭回归

import numpy as np
from sklearn.linear_model import Ridge
from sklearn import model_selection
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures

data = np.genfromtxt('Data/RidgeTestData01.txt', delimiter=',', skip_header=0)
plt.plot(data[:, 4])
# plt.show()
# data[:, :4] 指的是：所有行的前四列
X = data[:, :4]
y = data[:, 4]
poly = PolynomialFeatures(6)
X = poly.fit_transform(X)
train_set_X, test_set_X, train_set_y, test_set_y = model_selection.train_test_split(X, y, test_size=0.3, random_state=0)
clf = Ridge(alpha=1.0, fit_intercept=True)
clf.fit(train_set_X, train_set_y)
clf.score(test_set_X, test_set_y)
start = 1  # 接下来我们画一段200到300范围内的拟合曲线
end = 18
y_pre = clf.predict(X)  # 是调用predict函数的拟合值
time = np.arange(start, end)
plt.plot(time, y[start:end], 'b', label="real")
plt.plot(time, y_pre[start:end], 'r', label='predict')
# 展示真实数据（蓝色）以及拟合的曲线（红色）
plt.legend(loc='upper lef')  # 设置图例的位置
plt.show()

