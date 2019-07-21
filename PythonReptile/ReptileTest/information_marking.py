#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/7/21 0021 下午 8:33
# @Author: XieHaoHao
# @File  : information_marking.py
# 信息标记：XML，JSON，YAML

import requests
from bs4 import BeautifulSoup
import re   # 引入正则表达式库

try:
    url = 'https://python123.io/ws/demo.html'
    user_agent = {'user_agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=user_agent)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    demo = r.text
except:
    print('爬取内容失败！')


# 获取HTML页面中所有<a>标签中的URL链接地址
def get_url():
        soup = BeautifulSoup(demo, 'html.parser')
        for link in soup.find_all('a'):     # 查找所有的a标签
            print(link.get('href'))     # 获得href属性的值


# 获得标签的几种方法
def get_content():
    soup = BeautifulSoup(demo, 'html.parser')
    soup.find_all('a')
    soup.find_all(['a', 'b'])

    # 获得所有标签
    for tag in soup.find_all('True'):
        print(tag.name)
    for tag in soup.find_all(re.compile('b')):   # 正则表达式表示以'b'开头
        print(tag.name)
    soup.find_all('p', 'course')    # 查找p标签中包含course的p标签
    soup.find_all(id='link1')       # 查找id属性值为link1的标签
    soup.find_all('a', recursive='False')   # 如果不写recursive='False'则默认查找soup节点下的子孙节点，否则只查找子节点
    # 对字符串域进行检索
    soup.find_all(string='Basic Python')


if __name__ == '__main__':
    get_url()
