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
import requests
import xlwt  # excel
import pymysql


def spider():
    baseurl = "http://suumo.jp/library/tf_13/sc_13123/p_"
    getData(baseurl)


def getData(baseurl):
    jsonList = []
    i = 1
    while True:
        dataList = askUrl(baseurl + str(i))
        jsonList.extend(dataList)
        i += 1
        if dataList == '':
            # if i == 2:
            break
    return jsonList


def askUrl(url):
    jsons = []
    # 封装request  伪造浏览器客户端
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36",
    }

    try:
        response = requests.get(url=url, headers=headers).text
        bs = BeautifulSoup(response, "html.parser")
        trs = bs.select("tbody tr")
        jsons = build(trs)
    except Exception as e:
        print(f'{e}')
    return jsons


def build(trs):
    list = []
    for i in range(0, len(trs)):
        if i == 0:
            pass
        else:
            data = {"img": '', "name": "", "detailUrl": "", "walkTime": '', "buildTime": ''}
            tds = trs[i].find_all("td")
            # bs4.element.Tag
            print(type(trs[i]))
            for n in range(0, len(tds)):
                if n == 0:
                    data['img'] = tds[n].img.attrs['src']
                if n == 1:
                    data['name'] = tds[n].find(class_="mT9").string
                    data['detailUrl'] = tds[n].find("a").attrs["href"]
                if n == 2:
                    data['walkTime'] = tds[n].string
                if n == 4:
                    data['buildTime'] = tds[n].string
            list.append(data)
    print(list)
    # savaData(list)
    return list


def savaData(list):
    conn = pymysql.connect(host='localhost', user='root', password="159629zxc", db='summo', charset="UTF8")
    cursor = conn.cursor()
    for data in list:
        sql = "INSERT INTO `house`(`name`,`img`,`detailUrl`,`walkTime`,`buildTime`) VALUES ('%s', '%s', '%s', '%s', '%s' )" % (
            data['name'], data['img'], data['detailUrl'], data['walkTime'], data['buildTime'])
        print(sql)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            conn.commit()
        except Exception as e:
            print("出了异常:", e)
            conn.rollback()
    conn.close()


if __name__ == '__main__':
    spider()
