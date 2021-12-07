# coding: utf-8
import requests
from lxml import etree

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
}
# detail_text = requests.get('https://suumo.jp/chintai/bc_100261603251/',headers=headers).text
# detail_text = requests.get('https://suumo.jp/chintai/bc_100261682343/kankyo/',headers=headers).text
detail_text = requests.get('https://suumo.jp/chintai/bc_100260538216/',headers=headers).text

detail_tree = etree.HTML(detail_text)
title = detail_tree.xpath('//*[@class="panoramabox"]/iframe/@src')
print(title)
# dls = detail_tree.xpath('//*[@id="js-kankyo_photo_list"]//dl')
# for dl in dls:
#     dl_img = dl.xpath('.//dt/img/@src')[0].strip()
#     dl_title = dl.xpath('.//dd/text()')[0].strip()
#     print(dl_img)
#     print(dl_title)
