from sklearn.datasets import load_boston
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris


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
    city_name, city_data = load_rc_data('./Data/provinceData.txt')
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


# 使用 DBSCAN 对学生的上网开始时间和上网持续时间进行分析
def student_online_time_analysis():
    file = open('./Data/student.txt', 'r+', encoding='utf-8-sig')
    lines = file.readlines()
    mac_matching_time = dict()
    online_time_list = []

    for line in lines:
        mac = line.split(',')[2]
        start_time = int(line.split(',')[4].split(' ')[1].split(':')[0])
        online_time = int(line.split(',')[6])
        if mac not in mac_matching_time:
            mac_matching_time[mac] = len(online_time_list)
            online_time_list.append((start_time, online_time))
        else:
            online_time_list[mac_matching_time[mac]] = (start_time, online_time)

    # 以下一部分为开始上网时间的分析
    start_and_online_time = np.array(online_time_list).reshape((-1, 2))
    start_time_data = start_and_online_time[:, 0:1]

    db_scan = DBSCAN(eps=0.01, min_samples=2)
    db_scan_fit = db_scan.fit(start_time_data)
    labels = db_scan_fit.labels_

    labels_types = len(set(labels)) - (1 if -1 in labels else 0)

    result = [[] for i in range(labels_types)]
    for i in range(len(labels)):
        if labels[i] != -1:
            result[labels[i]].append(start_time_data[i][0])

    # 计算噪音比例
    noise_ratio = len(labels[labels[:] == -1]) / len(labels)
    # 分为n簇
    n_clusters_ = labels_types
    # 衡量指标
    judge = metrics.silhouette_score(start_time_data, labels)

    for i in range(labels_types):
        print('第', i, '簇：')
        print(start_time_data[labels == i].flatten())

    plt.hist(result, 24)
    plt.show()

    # 以下为对上网时长的分析
    duration_time = np.log(1+start_and_online_time[:, 1:])
    dt_db_scan = DBSCAN(eps=0.5, min_samples=2)
    dt_db_scan_fit = dt_db_scan.fit(duration_time)
    dt_labels = dt_db_scan_fit.labels_
    dt_result = [[] for i in range(len(set(dt_labels)) - (1 if -1 in dt_labels else 0))]

    for i in range(len(set(dt_labels)) - (1 if -1 in dt_labels else 0)):
        dt_result[i] = start_and_online_time[:, 1:][[dt_labels == i]].flatten()
        # 计算上网持续时间的均值和标准差
        duration_time_mean = np.mean(dt_result[i])
        duration_time_std = np.std(dt_result[i])


def iris_analysis():
    iris_data_x, iris_data_y = load_iris(return_X_y=True)
    iris_pca = PCA(n_components=2)
    iris_fit = iris_pca.fit_transform(iris_data_x)
    print()


iris_analysis()




