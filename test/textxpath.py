# coding: utf-8
import requests
from lxml import etree

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
}
# detail_text = requests.get('https://suumo.jp/chintai/bc_100261603251/',headers=headers).text
detail_text = requests.get('https://suumo.jp/chintai/bc_100260916090/',headers=headers).text

detail_tree = etree.HTML(detail_text)
# title = detail_tree.xpath('//*[@id="contents"]/div[2]/table//tr[1]/td[2]/text()')
title = detail_tree.xpath('//iframe//html')
print(title)