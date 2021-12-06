# coding: utf-8

import requests

if __name__ == '__main__':
    url = 'https://suumo.jp/front/gazo/fr/bukken/547/100252795547/100236649077_gt.jpg'
    # 获取二进制图片数据
    response = requests.get(url).content
    """
     ========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
    ========= ===============================================================
    """
    with open('image.jpg', 'wb') as fp:
        fp.write(response)
