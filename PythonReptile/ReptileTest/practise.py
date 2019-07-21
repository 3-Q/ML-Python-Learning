#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/7/21 0021 下午 5:05
# @Author: XieHaoHao
# @File  : practise.py
import requests
import os


# 访问亚马逊
def visit_amazon(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=kv)
        # response中含有我发送的request请求
        r.request.headers
        r.status_code
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        text = r.text[1000:2000]
        return text
    except:
        return '发现异常'


# 访问百度
def visit_baidu(url, kw):
    try:
        kv = {'wd': kw}
        user_agent = {'user-agent': 'Mozilla/5.0'}
        # 设置虚假的浏览器版本，设置查询的关键字
        r = requests.get(url, params=kv, headers=user_agent)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        r.request.url
        print(len(r.text))
    except:
        return '出现异常'


# 从网上下载图片并保存
def picture_save(url, location):
    try:
        file_name = url.split('/')[-1]
        file_path = location + file_name
        # 判断当前是否存在location路径
        if not os.path.exists(location):
            os.mkdir(location)
        if not os.path.exists(file_path):
            user_agent = {'user-agent': 'Mozilla/5.0'}
            r = requests.get(url, headers=user_agent)
            # 首先用open创建/打开文件，在利用write写入内容
            with open(file_path, 'wb') as f:
                f.write(r.content)
                f.close()
                print('文件保存成功！')
        else:
            print('文件已存在！')
    except:
        return "爬取失败！"


def ip_location(ip):
    try:
        user_agent = {'user-agent': 'Mozilla/5.0'}
        url = 'http://www.ip138.com/ips138.asp?'
        kv = {'ip': ip}
        r = requests.get(url, params=kv, headers=user_agent)
        r.status_code
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        r.request.url
        print(r.text[-1000:])  # 表示返回最后500个字节
    except:
        return '爬虫失败！'


if __name__ == "__main__":
    amazon_url = "https://www.amazon.cn"
    # visit_amazon(amazon_url)

    baidu_url = "http://www.baidu.com/s"
    # visit_baidu(baidu_url, 'python')

    picture_url = "http://img3.duitang.com/uploads/item/201511/07/20151107181116_CYwhJ.thumb.700_0.jpeg"
    picture_save_location = "C:\\Users\\Administrator\\Pictures\\Saved Pictures\\"
    # picture_save(picture_url, picture_save_location)

    ip = '112.101.12.15'
    ip_location(ip)


