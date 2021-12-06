# coding: utf-8
import time

import requests
from lxml import etree

if __name__ == '__main__':
    count = 0
    url = 'https://news.yahoo.co.jp/polls/domestic/42861/result'
    url2 = 'https://news.yahoo.co.jp/polls/domestic/42861/vote'

    headers = {
        # ':authority': 'news.yahoo.co.jp',
        # ':method': 'POST',
        'q': '0.8',
        # 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        # 'content-type': 'application/x-www-form-urlencoded',
        'cookie': '',
        'origin': 'https://news.yahoo.co.jp',
        'referer': 'https://news.yahoo.co.jp/polls/domestic/42861/vote',
        # 'pragma': 'no-cache',
        # 'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
    }

    proxy={'http': "211.65.197.93:80"}
    response = requests.get(url, headers=headers, proxies=proxy)
    print(response.headers)
    cookie = response.headers.get("Set-Cookie").split(";")[0]
    headers['cookie'] = cookie

    response = requests.get(url2, headers=headers, proxies=proxy)
    # text.encoding = 'utf-8'
    tree = etree.HTML(response.text)
    name = tree.xpath('//*[@id="vote"]/form/input/@value')[0]
    params = {
        'answer': '3',
        '.crumb': name,
        'voteButton': ''

    }
    print(name)
    print(params)
    response = requests.post(url, headers=headers, proxies=proxy, params=params, timeout=5, )
    print(response.headers)
    # while count <= 1000:
    # response = requests.post(url, headers=headers, proxies={'http': '182.84.145.121:3256'}, params=params,
    #                          timeout=5, )
    # time.sleep(1)
    # string = text.encode('iso-8859-1').decode('utf-8')
    # with open('ip.html', 'w', encoding='utf-8') as fp:
    #     fp.write(text)
    # 7400
    # count += 1
    # print(response)
    # print(response, count);
'''

answer: 3
.crumb: AkFvqWEATJj1Q1fM1x3VjcZSOy1SO5D8GuSJw7SUSJsNY-o4pXPGJUlA9z_DBjeH0_bu9jCvBrHj7X_Q7gMnkkefayJyQFmPOeconc7YYPquwisLuirv0sBZVh3HyexJYeUq-kLH
voteButton: 
    
yhlVer: 2
yhlClient: rapid
yhlS: 590208868
format: json
yhlCT: 2
yhlBTMS: 1638493733070
yhlClientVer: 4.1.0
yhlRnd: 3TLL06ji3gTEOKh3kwpov3ri
yhlCompressed: 3


:authority: news.yahoo.co.jp
:method: POST
:path: /polls/domestic/42861/result
:scheme: https
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7
cache-control: no-cache
content-length: 164
content-type: application/x-www-form-urlencoded
cookie: B=a89u52dg99kbs&b=3&s=26; XB=a89u52dg99kbs&b=3&s=26; A=a89u52dg99kbs&sd=B&t=1620365692&u=1620518370&v=1; XA=a89u52dg99kbs&sd=B&t=1620365692&u=1620518370&v=1; JV=A8aIqGEAADITj3p2B7a43BFvH21n-kllh-c3xFHiGh-_Oq1x4cSqf2QGyqaa0tigXGR-gYbWJKZHGyKGzKkk6X763Mk3s8fAlMmgC9mk_SZaZwx9HggT9DrQhIgWairQGPudEZZ7bj-KMoNEXczwetuj3IP2HRNeqmgFI9V_NB6_SxrUMoWabMFbgZILKRRPGxSUTpkYLwoZKjTv-8rfKxJaR0pwj2tkmEopzyqEhVKKPzDl8nr7LkI0gtuesVIoL6elvAPs4bIoHhZhy1RW0iuxvTvRyIj5qvr9Pt3DAtTuEceCTA5zJsT3naO5kyWEFLKqKaWc5d3PRxYvXT0VwmJt9YS-_kC0x4SH882Z4Nd7ykxtmmJXm0_QzKfqfZbXt4Wi189ZIRi-ucOPljNhTDf9nwVh4tZaFEEMwrDcW2MwPQy50793xKptcGKXCNgnlfJJaJDhy4yqikKja-SKW_JQHTvAouJ-wFWOdlzcnqiWBTj7w6EAUU4K4cLr6KXcUQpInObI9lEaiKvgk4Og1L7utojlP0WHSaw5eAvT4mjzQZE3JPnVLV-cT9LUcm5KMjybfQ56UXZTihlol_HeG0UtazgBwgvyR6hSdnWRyb8lJS0A6PM&v=2
origin: https://news.yahoo.co.jp
pragma: no-cache
referer: https://news.yahoo.co.jp/polls/domestic/42861/vote
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36
'''
