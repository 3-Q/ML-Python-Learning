#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/6/16 0016 下午 7:28
# @Author: XieHaoHao
# @File  : ClassificationTest01.py
"""
读取特征文件
数据预处理
K近邻分类器
决策树分类器
高斯朴素贝叶斯分类器
"""


import pandas as pd
import numpy as np

from sklearn.preprocessing import Imputer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB


def load_datasets(feature_paths, label_paths):
    feature = np.ndarray(shape=(0, 3))
    label = np.ndarray(shape=(0, 1))
    for file in feature_paths:
        df = pd.read_table(file, delimiter=',', na_values='?', header=None)
        imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
        imp.fit(df)
        df = imp.transform(df)
        feature = np.concatenate((feature, df))

    for file in label_paths:
        df = pd.read_table(file, header=None)
        label = np.concatenate((label, df))

    label = np.ravel(label)
    return feature, label


if __name__ == '__main__':
    ''' 数据路径 '''
    featurePaths = ['Data/human1.feature', 'Data/human2.feature', 'Data/human3.feature']
    labelPaths = ['Data/label01.label', 'Data/label02.label', 'Data/label03.label']
    ''' 读入数据  '''
    x_train, y_train = load_datasets(featurePaths[:2], labelPaths[:2])
    x_test, y_test = load_datasets(featurePaths[2:], labelPaths[2:])
    x_train, x_, y_train, y_ = train_test_split(x_train, y_train, test_size=0.0001)

    print('Start training knn')
    knn = KNeighborsClassifier().fit(x_train, y_train)
    print('Training done')
    answer_knn = knn.predict(x_test)
    print('Prediction done')

    print('Start training DT')
    dt = DecisionTreeClassifier().fit(x_train, y_train)
    print('Training done')
    answer_dt = dt.predict(x_test)
    print('Prediction done')

    print('Start training Bayes')
    gnb = GaussianNB().fit(x_train, y_train)
    print('Training done')
    answer_gnb = gnb.predict(x_test)
    print('Prediction done')

    print('\n\nThe classification report for knn:')
    print(classification_report(y_test, answer_knn))
    print('\n\nThe classification report for DT:')
    print(classification_report(y_test, answer_dt))
    print('\n\nThe classification report for Bayes:')
    print(classification_report(y_test, answer_gnb))