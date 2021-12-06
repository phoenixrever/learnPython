# coding: utf-8

import requests
import re
import os

def getImages(id):
    url = f'https://www.tupianzj.com/meinv/20210831/232011{id}.html'
    # 获取二进制图片数据
    print(url)
    response = requests.get(url).text
    """
    <img src="https://img.lianzhixiu.com/uploads/allimg/202108/9999/e7878799b9.jpg"
     id="bigpicimg" alt="紧身包臀裙美少妇高跟美腿套图">
    """
    # ()内就是想要获取的内容
    ex = '<img src="(.*?)" id="bigpicimg" alt=.*?'
    text = re.findall(ex, response, re.S)
    print(text)
    return text


if __name__ == '__main__':
    i = 1
    id = ''
    while True:
        if i == 1:
            id = ''
        else:
            id = '_' + str(i)
        i += 1
        response = getImages(id)
        if len(response) == 0:
            break
        image = requests.get(response[0]).content
        if not os.path.exists('images'):
            os.mkdir('images')
        with open(f"images/image{id}.jpg", 'wb') as fp:
            fp.write(image)
