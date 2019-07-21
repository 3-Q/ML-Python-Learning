#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/7/21 0021 下午 12:02
# @Author: XieHaoHao
# @File  : requestsLibraryTest.py
import requests


def requests_test01(types):
    # request、get、post、head、put、patch、delete等方法有诸多参数
    # requests的request方法
    if types == 'request':
        kv = {'key1': 'value1'}
        hd = {'user-agent': 'Chrome/10'}
        fs = {'file': open('Data/student.txt', 'rb')}
        pxs = {'http': 'http://user:pass@10.10.10.1.:1234', 'https': 'https://10.10.10.1:4321'}
        r = requests.request('POST', 'http://httpbin.org/post', params=kv, data=kv, json=kv, headers=hd, files=fs, timeout=10, proxies=pxs)
        print(r.url)

    # requests的get方法
    if types == 'get':
        baidu_get = requests.get('http://www.baidu.com')
        status = baidu_get.status_code
        baidu_get.encoding = 'utf-8'

    # requests的head方法
    if types == 'head':
            baidu_head = requests.head('http://www.baidu.com')
            baidu_head.headers      # 可以获得headers，不能获得text
            baidu_head.text

    # requests的post方法，将post的内容添加在URL内容所在位置的后面，当post键值对时，会默认放到表单下，提交为字符串时，会放到data的字段下
    if types == 'post':
        baidu_post = {'key1': 'value1', 'key2': 'value2'}
        response_post = requests.post('http://httpbin.org/post', baidu_post)
        print(response_post.text)

    # requests的put方法，会将原有的URL内容覆盖掉
    if types == 'put':
        baidu_put = 'this is a string'
        response_put = requests.put('http://httpbin.org/put', baidu_put)
        print(response_put.text)


# 爬取网页的通用代码框架
def get_html_url(url):
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()     # 重点：如果状态码不是200，就会抛出异常
        response.encoding = response.apparent_encoding
        return response.text
    except:
        return "产生异常"


if __name__ == "__main__":
    # baidu_url = "http://www.baidu.com"
    # print(get_html_url(baidu_url))

    requests_test01('request')

