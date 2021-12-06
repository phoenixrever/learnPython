# coding: utf-8

def fun():
    print("hello")


try:
    f = open("baidu.html", 'r')
    print(f.read())
except Exception as e:
    print("出了异常:", e)
    exit(-1)
finally:
    f.close()

with open("baidu.html", 'r') as fo:
    fo.read()
