# coding: utf-8
import time

from lxml import etree
import requests
from requests.adapters import HTTPAdapter
import urllib.parse
import pymysql

my_request = requests.Session()
my_request.mount('http://', HTTPAdapter(max_retries=5))
my_request.mount('https://', HTTPAdapter(max_retries=5))


def getData(url):
    global text, title, a, location, name, params, img
    text = my_request.get(url, params=params, headers=headers, timeout=5, ).text
    tree = etree.HTML(text)
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
                print(url_detail)
                detail_text = my_request.get(url_detail, params=params, headers=headers).text
                time.sleep(1)
                detail_tree = etree.HTML(detail_text)
                title = detail_tree.xpath('//*[@class="section_h1-header-title"]/text()')[0].strip()
                # 是否是重复数据
                select_sql = "select * from house where title = '%s'" % (title)
                # print(select_sql)
                cursor.execute(select_sql)
                results = cursor.fetchall()
                if (len(results) > 0):
                #     exit(0)
                    continue

                price = detail_tree.xpath(
                    '//*[@id="js-view_gallery"]/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/text()')[
                    0].strip()
                # print(price)
                management_price = detail_tree.xpath(
                    '//*[@id="js-view_gallery"]/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div[2]/text()')[
                    0].strip()
                gift_price = detail_tree.xpath(
                    '//*[@id="js-view_gallery"]/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/ul/li[1]/div/div[2]/span[3]/text()')[
                    0].strip()
                deposit = detail_tree.xpath(
                    '//*[@id="js-view_gallery"]/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/ul/li[2]/div/div[2]/text()')[
                    0].strip()
                room = detail_tree.xpath(
                    '//*[@id="js-view_gallery"]/div[1]/div[2]/div[3]/div[1]/div/div[2]/ul/li[1]/div/div[2]/text()')[
                    0].strip()
                area = detail_tree.xpath(
                    '//*[@id="js-view_gallery"]/div[1]/div[2]/div[3]/div[1]/div/div[2]/ul/li[2]/div/div[2]/text()')[
                    0].strip()
                direction = detail_tree.xpath(
                    '//*[@id="js-view_gallery"]/div[1]/div[2]/div[3]/div[1]/div/div[2]/ul/li[3]/div/div[2]/text()')[
                    0].strip()
                classify = detail_tree.xpath(
                    '//*[@id="js-view_gallery"]/div[1]/div[2]/div[3]/div[1]/div/div[2]/ul/li[4]/div/div[2]/text()')[
                    0].strip()
                age = detail_tree.xpath(
                    '//*[@id="js-view_gallery"]/div[1]/div[2]/div[3]/div[1]/div/div[2]/ul/li[5]/div/div[2]/text()')[
                    0].strip()
                access = detail_tree.xpath(
                    '//*[@id="js-view_gallery"]/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[2]//text()')
                access_list = []
                for a in access:
                    if a.strip() != '':
                        access_list.append(a.strip())
                walk_time = ','.join(access_list)
                location = detail_tree.xpath(
                    '//*[@id="js-view_gallery"]/div[1]/div[2]/div[3]/div[2]/div[2]/div/div[2]/div/text()')[0].strip()
                # print('walk_time', walk_time)

                # 部屋の特徴・設備 room_decoration
                room_decoration = detail_tree.xpath('//*[@id="bkdt-option"]/div/ul/li/text()')[0].strip()
                # 物件概要
                detail_room = ''
                build_material = ''
                build_date = ''
                car_park = ''
                floor = ''
                depreciation = ''
                check_in = ''
                requirement = ''
                total_house = ''
                house_update = ''
                duration = ''
                commission = ''
                company_price = ''
                total_price = ''
                other_price = ''
                remarks = ''
                tables = detail_tree.xpath('//*[@id="contents"]//table//tr')
                for index, tr in enumerate(tables):
                    if index > 6:
                        name = tr.xpath('.//th/text()')
                        if len(name) != 0 and name[0].strip() == '契約期間':
                            duration = tr.xpath('.//td/ul/li/text()')[0].strip()
                        if len(name) != 0 and name[0].strip() == '仲介手数料':
                            commission = tr.xpath('.//td/ul/li/text()')[0].strip()
                        if len(name) != 0 and name[0].strip() == '保証会社':
                            company_price = tr.xpath('.//td/ul/li/text()')[0].strip()
                        if len(name) != 0 and name[0].strip() == 'ほか初期費用':
                            total_price = tr.xpath('.//td/ul/li/text()')[0].strip()
                        if len(name) != 0 and name[0].strip() == 'ほか諸費用':
                            other_price = tr.xpath('.//td/ul/li/text()')[0].strip()
                        if len(name) != 0 and name[0].strip() == '備考':
                            remarks = tr.xpath('.//td/ul/li/text()')[0].strip()
                    else:
                        if index == 0:
                            detail_room = tr.xpath('.//td[1]/text()')[0].strip()
                            build_material = tr.xpath('.//td[2]/text()')[
                                0].strip()
                        if index == 1:
                            floor = tr.xpath('.//td[1]/text()')[0].strip()
                            build_date = tr.xpath('.//td[2]/text()')[
                                0].strip()
                        if index == 2:
                            depreciation = tr.xpath('.//td[1]/text()')[
                                0].strip()
                            car_park = tr.xpath('.//td[2]/text()')[
                                0].strip()
                        if index == 3:
                            check_in = tr.xpath('.//td[1]/text()')[
                                0].strip()
                        if index == 4:
                            requirement = tr.xpath('.//td[1]/text()')[
                                0].strip()
                        if index == 5:
                            total_house = tr.xpath('.//td[2]/text()')[
                                0].strip()
                        if index == 6:
                            house_update = tr.xpath('.//td[1]/text()')[
                                0].strip()

                # vr预览图的 有的页面是没有
                iframe = detail_tree.xpath('//*[@id="contents"]/div[2]/div[2]/div/iframe/@src')
                vr_image = ''
                vr_link = ''
                if len(iframe) != 0:
                    # print(iframe[0].strip())
                    vr_link = iframe[0].strip()
                # 数据库插入数据
                house_sql = "insert into house(title, price, management_price, gift_price, deposit, room, area," \
                            "direction,classify, age, walk_time, location, vr_image, vr_link, room_decoration," \
                            "detail_room, build_material, floor, build_date, depreciation, car_park, check_in," \
                            "requirement,total_house, house_update,duration, commission, company_price, " \
                            "total_price,other_price, remarks)" \
                            " values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                title, price, management_price, gift_price, deposit, room, area, direction, classify, age, walk_time,
                location, vr_image, vr_link, room_decoration, detail_room, build_material, floor, build_date,
                depreciation, car_park, check_in, requirement, total_house, house_update, duration, commission,
                company_price, total_price, other_price, remarks)
                print(house_sql)
                cursor.execute(house_sql)

                house_id = cursor.lastrowid
                db.commit()

                # ============所有图片 单独的表====================
                # 所有图片
                house_images = []
                images = detail_tree.xpath('//*[@id="js-view_gallery-list"]//img/@data-src')
                image_sql = 'insert into image values'
                for image in images:
                    house_images.append(image.strip())
                    image_sql = image_sql + '(' + 'null,' +"'"+ image.strip() +"'"+ ",'" + str(house_id) + "'),"
                print(image_sql.strip(','))
                cursor.execute(image_sql.strip(','))
                db.commit()

                # vr封面
                vr_image = house_images[0]
                # =============================================

                # =================  周辺環境表 里面有地图 经纬度===================
                nearUrl = detail_tree.xpath('//*[@class="data_around"]//a/@href')[0].strip()
                print(nearUrl)
                near_text= my_request.get('https://suumo.jp' + nearUrl, params=params, headers=headers, timeout=5).text
                time.sleep(2)
                nearTree = etree.HTML(near_text)

                # 地图
                action = nearTree.xpath('//*[@id="js-timesForm"]/@action')[0].strip()
                o = urllib.parse.urlparse(action)
                params = urllib.parse.parse_qs(o.query)
                print(params)
                map_longitude = params.get('ido')[0]
                map_latitude = params.get('keido')[0]
                # 周边
                dls = nearTree.xpath('//*[@id="js-kankyo_photo_list"]//dl')
                print(dls)
                near_sql = 'insert into neighborhood values'
                for dl in dls:
                    dl_img = dl.xpath('.//dt/img/@src')[0].strip()
                    dl_title = dl.xpath('.//dd/text()')[0].strip()
                    print(dl_img)
                    print(dl_title)
                    near_sql = near_sql + '(' + 'null,' + "'"+dl_img+"'" + ',' + "'"+dl_title+"'" + ',' + "'"+str(house_id)+"'" + '),'
                print(near_sql.strip(','))

                # cursor.execute(near_sql.strip(','))
                db.commit()

                # 插入house 表
                cursor.execute("update house set vr_image='%s',map_longitude='%s',map_latitude='%s' where id=%d" % (
                    vr_image, map_longitude, map_latitude, house_id))
                db.commit()
                print(title, price, management_price, gift_price, deposit, room, area, direction,
                      classify, age, walk_time, location, vr_image, vr_link, room_decoration,
                      detail_room, build_material, floor, build_date, depreciation, car_park, check_in,requirement,
                      total_house, house_update, duration, commission, company_price, total_price,
                      other_price, remarks, map_longitude, map_latitude)
        except Exception as e:
            print(e.with_traceback())
            pass
        continue

if __name__ == '__main__':

    # db = pymysql.connect(host='localhost', user='root', password='159629zxc', database='summo')
    db = pymysql.connect(host='192.168.56.100', user='root', password='root', database='summo')
    cursor = db.cursor()
    url = 'https://suumo.jp/jj/chintai/ichiran/FR301FC005/?ar=030&bs=040&ra=013&rn=0065&ek=006534520&cb=0.0&ct=5.0&mb=0&mt=9999999&et=9999999&cn=9999999&shkr1=03&shkr2=03&shkr3=03&shkr4=03&sngz=&po1=25&po2=99&pc=10&page='

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
    }
    params = {
    }
    page = 1

    while page < 3:
        getData(url+ (str(page)))
        page += 1
