# coding: utf-8

from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    url = 'https://www.umei.cc/p/gaoqing/cn/235649.htm'
    response = requests.get(url)
    # 防止乱码
    response.encoding = 'utf-8'
    text = response.text
    bs = BeautifulSoup(text, 'html.parser')
    print(bs.title.string)  # 返回第一次出现的li 的文本 string/text/get_text()
    """
    text/get_text() 获取标签下的所有文本内容
    string 只是此标签的文本
    """
    print(bs.li)  # 返回第一次出现的li
    print(bs.li.a.text)  # 返回第一次出现的li 里面的a元素的文本
    print(bs.li.attrs['id'])  # 返回第一次出现的li 的id属性
    print(bs.find("li"))  # 返回第一次出现的li
    # print(bs.find_all("li"))  # findAll 返回全部的li
    # tag 可以有attrs属性 也可以直接[] 获取
    print(bs.find_all('div', class_='Pix-box')[0].img.attrs['src'])
    print(bs.find_all('div', class_='Pix-box')[0].img['src'])

    # 元素选择器 返回数组
    print(bs.select("li .Pix-box"))
    # print(bs.select("#u1"))  # id
    # print(bs.select("a[name=tj_login]"))
    # print(bs.select("head a"))
    # print(bs.select("head a").get_text())
