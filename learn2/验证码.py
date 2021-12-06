# coding: utf-8

"""
使用session 模拟登陆请求 对象自动存储cookie  这里验证码没搞好就
不要演示了 人工复制cookie就行

    sesson 储存服务器返回的set-cookie 在用次session发送请求
    session = requests.Session()
    session.get(url, headers=headers)
"""
import requests
from lxml import etree
import os

if __name__ == '__main__':
    url = 'https://dy.y15i6p5m.xyz/2048/read.php?tid-4229876.html'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
    }

    cookies = {
        'TDC_itoken': '2766748232%3A1578125692',
        '__51uvsct__JQCyGlULurppBEXr': '1',
        '__51vcke__JQCyGlULurppBEXr': '5daf8d6c-0829-58df-beaf-dfee4e9b1158',
        '__51vuft__JQCyGlULurppBEXr': '1632616293890',
        '__vtins__JQCyGlULurppBEXr': '%7B%22sid%22%3A%20%2252b6d31f-59de-59ab-9a57-16f5a6919dd6%22%2C%20%22vd%22%3A%2018%2C%20%22stt%22%3A%20911791%2C%20%22dr%22%3A%20123053%2C%20%22expires%22%3A%201632619005674%2C%20%22ct%22%3A%201632617205674%7D',
        'a22e7_ck_info': '%2F%09',
        'a22e7_cknum': 'UlBQAFUAUlFZVW86UgFWDwsBBlcAC1UEVlUEAFAEVVcBVl0AAlNbCgUFAlU%3D',
        'a22e7_lastpos': 'T4229876',
        'a22e7_lastvisit': '156%091632617198%09%2F2048%2Fread.php%3Ftid-4229876.html',
        'a22e7_ol_offset': '210975',
        'a22e7_readlog': '2C4232757',
        'a22e7_threadlog': '	%2C23%2C27%2C',
        'a22e7_winduser': 'UVRQA1cJUmwAUgMFDgdWAFwFBQJRV1AFVwZXBVUCAAJSBVtWAVcACmo%3D',
        'zh_choose': 'n'
    }

    response = requests.get(url, headers=headers, cookies=cookies)
    text = response.text
    tree = etree.HTML(text)
    srcs = tree.xpath('//*[@id="read_tpc"]/img/@src')
    for i in range(0, len(srcs)):
        print(srcs[i])
        img = requests.get(srcs[i]).content
        if not os.path.exists('images'):
            os.mkdir('images')
        with open(f'images/image_{i}.jpg', 'wb') as fp:
            fp.write(img)
    print('over')
