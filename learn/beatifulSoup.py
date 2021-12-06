# coding: utf-8
from http.client import HTTPResponse

'''
 网页解析 获取数据  BeautifulSoup 将复杂的html文本转化成一个复杂的树形结构
 每个节点都是python 对象 ,所有对象可归纳为3种
 1) Tag
 2) NavigableString
 3) BeautifulSoup
 4) Comment
'''
from bs4 import BeautifulSoup

import re  # 正则表达式
import urllib.request  # 发送http
import urllib.parse  # 发送http


# coding: utf-8

def test():
    try:
        baseurl = "http://www.baidu.com"
        # 封装request  伪造浏览器客户端
        request = urllib.request.Request(url=baseurl, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36",
        }, method="GET")
        response = urllib.request.urlopen(request, timeout=3)  # type: HTTPResponse
        html = response.read().decode("utf-8")
        # ===============BeautifulSoup 解析python tree===========
        '''
        ("lxml","lxml-xml", "html.parser", or "html5lib")
        '''
        bs = BeautifulSoup(markup=html, features="html.parser")  # type:
        # print(bs.title.string)  # string 标签内容
        # print(bs.a.string)  # 第一个tag 输出会把注释内容替换掉
        # print(bs.a.attrs)
        # print(type(bs.head))  # <class 'bs4.element.Tag'>

        # 文档  具体方法见详细文档 https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/
        # print(bs.prettify())

        # print(bs.get_text())  # 从文档中获取所有文字内容:

        # 文档的搜索

        # print(bs.find_all("a")) #查找完全匹配a 标签的内容
        # 正则表达式
        # print(bs.find_all(re.compile("a")))  # 只要包含a字符串的tag
        # print(bs.find_all(name_is_exsits))  # 搜索出有用含有name 属性的tag

        # keyword args 参数  class_ 代表有class属性
        # list = bs.find_all(class_=True)
        # list = bs.find_all(class_="text-color")
        # list = bs.find_all(id="head")
        # 文本 text
        # list = bs.find_all(text=["重庆西南大学一返渝学生核酸异常", "地图", "贴吧"])  # 精确匹配必须完全一样
        list = bs.find_all(text=re.compile("重庆"))  # 正则 模糊匹配
        for item in list:
            print(item)

        # 元素选择器
        print(bs.select("title"))
        print(bs.select("#u1"))  # id
        print(bs.select("a[name=tj_login]"))
        print(bs.select("head a"))  # id
        print(bs.select("head a").get_text())  # id

        print(bs.find_all('div', class_="item")) #查找class 为item的div
    except Exception as e:
        print(f'{e}')


# 搜索出有用含有name 属性的tag
def name_is_exsits(tag):
    return tag.has_attr("name")


if __name__ == '__main__':
    test()
