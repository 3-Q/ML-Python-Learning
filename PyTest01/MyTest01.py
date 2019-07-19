from sklearn.datasets import load_boston
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans


# 对加载数据集的测试
def analytical_dataset_1():
    boston_dataset = load_boston()
    print(boston_dataset.data.shape)
    print(boston_dataset.target.shape)


# 对加载数据集的测试
def analytical_dataset_2():
    boston_data, boston_target = load_boston(return_X_y=True)
    print(boston_data.shape)
    print(boston_target.shape)


# 对加载数据集的images的测试
def analytical_digits_dataset_1():
    digits = load_digits(n_class=9)
    print(digits.images.shape)
    plt.matshow(digits.images[0])
    plt.matshow(digits.images[1500])
    plt.show()


# 使用 K-means 聚类算法来实现对多个省市的居民消费情况的聚类
def resident_consumption():
    city_name, city_data = load_rc_data('Data\\provinceData.txt')
    km = KMeans(n_clusters=2)
    label = km.fit_predict(city_data)   # label是对每条数据做了一个标记（类别）
    result = [[], []]
    for i in range(len(city_name)):
        result[label[i]].append(city_name[i])
    consumption = np.sum(km.cluster_centers_, axis=1)
    for i in range(len(result)):
        print("%.2f" % consumption[i], "%.3f" % 12.1)
        print(result[i])


def load_rc_data(file_path):
    file = open(file_path, 'r+', encoding='utf-8-sig')  # encoding不可以不加，否则file.readlines()运行错误
    lines = file.readlines()
    city_name = []
    city_data = []
    for line in lines:
        split = line.split(",")
        city_name.append(split[0])
        city_data.append([float(split[i]) for i in range(1, len(split))])   # 二维数组的动态赋值
    return city_name, city_data


resident_consumption()


# boston_datas = load_boston()
# print(boston_datas.data.shape)

