# coding: utf-8
import urllib.request
import urllib.parse
from http.client import HTTPResponse


def test():
    # response = urllib.request.urlopen("http://www.baidu.com")
    # print(response.read().decode('utf-8'))

    # bytes 封装成字节数据流
    data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")
    try:
        response = urllib.request.urlopen("http://httpbin.org/post", data=data, timeout=3)  # type: HTTPResponse
        # assert isinstance(response, HTTPResponse) 声明式变量注解
        # print(response.read().decode("utf-8"))  # 可以格式化字符串
        print(response.status)
        print(response.getcode())
        print(response.getheaders())
    except Exception as e:
        print(f'{e}')


def test1():
    try:
        baseurl = "https://suumo.jp/library/tf_13/sc_13123/"
        # 封装request  伪造浏览器客户端
        request = urllib.request.Request(url=baseurl, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36",
        }, method="GET")
        response = urllib.request.urlopen(request, timeout=3)  # type: HTTPResponse
        print(response.read().decode("utf-8"))  # 可以格式化字符串
    except Exception as e:
        print(f'{e}')


if __name__ == '__main__':
    test1()
