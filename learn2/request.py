# coding: utf-8

import requests
import json

if __name__ == '__main__':
    # ===================get===================
    url = 'https://www.sogou.com/web'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36",
    }

    # params: (optional) Dictionary
    params = {
        'query': '美女',
    }
    response = requests.get(url, params=params, headers=headers)
    print(response.url)
    with open("sogou.html", mode='w', encoding='utf-8') as fp:
        fp.write(response.text)

    # ===================post===================
    post_url = 'https://fanyi.baidu.com/sug'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36",
    }

    # params: (optional) Dictionary
    data = {
        'kw': 'pussy',
    }
    response = requests.post(post_url, data=data, headers=headers)
    # 如果返回是json类型 转为json对象
    print(response.json())
    with open('json.json', 'w', encoding='utf-8') as fp:
        # 却又中文不要使用ascii码
        json.dump(response.json(), fp=fp, ensure_ascii=False, )
