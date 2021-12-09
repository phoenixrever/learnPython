# coding: utf-8
import time

import pymysql
import urllib.parse
from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
# 不打开浏览器
options.add_argument('--headless')
options.add_argument("--disable-gpu")
# options.add_argument('--blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
# 伪造请求 防止selenium 被监测到
options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 防止网站识别Selenium代码

browser = webdriver.Chrome(service=Service("../chromedriver.exe"), options=options)

browser.implicitly_wait(3)

# WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'section_h1-header-title')))
# WebDriverWait(browser, 3).until_not(EC.presence_of_element_located((By.ID, 'wrapper1')))


def my_request(link):
    browser.get(link)
    time.sleep(1)
    page_text = browser.page_source
    tree = etree.HTML(page_text)
    return tree



def getData(param):
    print(param)
    tree = my_request(param)
    groups = tree.xpath('//div[@class="property_group"]')
    for item in groups:
        try:
            # .// 表示当前节点下的元素
            # names = item.xpath('.//*[@class="property_inner-title"]/a/text()')
            hrefs = item.xpath('.//a[@class="js-cassetLinkHref"]/@href')
            # print(hrefs)
            # 详情页发送请求
            for i in range(0, len(hrefs)):
                time.sleep(2)
                url_detail = 'https://suumo.jp' + hrefs[i]
                summo_link=url_detail
                detail_tree = my_request(url_detail)
                title = detail_tree.xpath('//*[@class="section_h1-header-title"]/text()')
                if len(title) > 0:
                    title = title[0].strip()
                # 是否是重复数据
                select_sql = "select * from house where title = '%s'" % (title)
                # print(select_sql)
                cursor.execute(select_sql)
                results = cursor.fetchall()
                if len(results) > 0:
                    #     exit(0)
                    # continue
                    # vr预览图的 有的页面是没有
                    iframe = detail_tree.xpath('//*[@class="panoramabox"]/iframe/@src')
                    vr_link = ''
                    if len(iframe) != 0:
                        # print(iframe[0].strip())
                        vr_link = iframe[0].strip()

                    # 插入house 表
                    update_link = "update house set vr_link='%s',summo_link='%s' where title='%s'" % (
                        vr_link, summo_link, title)
                    print(update_link)
                    cursor.execute(update_link)
                    db.commit()
                    # print(title, price, management_price, gift_price, deposit, room, area, direction,
                    #       classify, age, walk_time, location, vr_image, vr_link, room_decoration,
                    #       detail_room, build_material, floor, build_date, depreciation, car_park, check_in,requirement,
                    #       total_house, house_update, duration, commission, company_price, total_price,
                    #       other_price, remarks, map_longitude, map_latitude)
        except Exception as e:
            print(e.with_traceback())
            pass
        continue


if __name__ == '__main__':
    # db = pymysql.connect(host='192.168.56.100', user='root', password='root', database='summo')
    db = pymysql.connect(host='localhost', user='root', password='159629zxc', database='summo')
    cursor = db.cursor()
    url = 'https://suumo.jp/jj/chintai/ichiran/FR301FC005/?ar=030&bs=040&ra=013&rn=0065&ek=006534520&cb=0.0&ct=5.0&mb=0&mt=9999999&et=9999999&cn=9999999&shkr1=03&shkr2=03&shkr3=03&shkr4=03&sngz=&po1=25&po2=99&pc=10&page='

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
    }
    # params = {
    # }
    proxies = {'http': '127.0.0.1:10808'}
    page = 49
    while page < 100:
        getData(url + (str(page)))
        page += 1
