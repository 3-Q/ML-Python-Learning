#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/7/21 0021 下午 6:39
# @Author: XieHaoHao
# @File  : beautiful_soup_learn.py
import requests
# 从bs4中导入了BeautifulSoup库
from bs4 import BeautifulSoup


# 对beautifulSoup库进行学习，获取soup的内容，bs4将读取的HTML文件都转为了utf-8编码
def beautiful_soup_learn():
    try:
        url = 'https://python123.io/ws/demo.html'
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=kv)
        r.status_code
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        demo = r.text
        soup = BeautifulSoup(demo, 'html.parser')
        print(soup.prettify())  # 打印soup的内容，prettify()可以被人类更好的阅读
        soup.title
        tag = soup.a
        print(tag.name)
        print(tag.parent.name)
        print(tag.attrs)
        print(tag.attrs['class'])
        type(tag.attrs)     # 标签的属性类型为dict
        type(tag)       # 标签的类型为标签类型
        print(tag.string)   # 获得标签对之间的字符串
    except:
        return '爬取内容失败'


# 标签树的下行遍历
def traverse_html_based_bs4_down():
    try:
        user_agent = {'user-agent': 'Mozilla/5.0'}
        url = 'https://python123.io/ws/demo.html'
        r = requests.get(url, headers=user_agent)
        r.status_code
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        demo = r.text
        soup = BeautifulSoup(demo, 'html.parser')

        # 标签树的下行遍历
        print(soup.body.contents)   # contents表示获得当前节点的子节点的所有信息，其中字符串'\n'也会看做为一个子节点
        print(len(soup.body.contents))
        print(soup.body.contents[3])
        # 遍历儿子节点：
        for child in soup.html.children:
            print(child)

        # 标签树的上行遍历
        for parent in soup.a.parents:
            if parent is None:
                print(parent)
            else:
                print(parent.name)  # 如果是soup本身，打印不出内容来，所以使用parent.name来打印soup

        # 标签树的平行遍历（平行遍历出的不一定是标签，也肯能是string，如：<p>china</p>，其中china就是一个string）
        soup.a.next_sibling     # 获得a标签的下一个平行标签（平行标签只能是在相同的父节点下的）
        soup.a.previous_sibling     # 获得a标签的上一个平行标签
        # 标签树的平行遍历
        for sibling in soup.a.next_siblings:    # next_siblings为迭代平行遍历，是所有的下行标签集合，只能用在for循环的语句中
            print(sibling)
    except:
        return '爬取失败！'


if __name__ == '__main__':
    # beautiful_soup_learn()
    traverse_html_based_bs4_down()
