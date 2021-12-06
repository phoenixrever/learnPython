# coding:utf-8

import keyword
import random

"""
三引号注释
"""
print(keyword.kwlist)

name = '橋本美波'
age = 20
print(type(age))
print("私わ二十歳%dです" % age)
print("私わ二十歳です" + name)
print("名前は%s ,年齢%d:" % (name, age))  # 连接字符串用 %
print('www', 'baidu', 'com', sep='.')  # www.baidu.com

# end表示末尾追加 不换行
print("hello", 'world', end='')

# password = input('请输入密码:')
# print('您输入的密码是:', password)
# print(type(password))  # <class 'str'>

b = '10'
print(b * 10)  # 会输出多个10
print(int(b) * 10)  # 强制类型转换 会输出100

print(10 ** 2)  # 10的二次幂 100
print(10 // 3)  # 10除以3 向下取整 3

# =============随机数=================
print(random.randint(0, 10))  # [0-10]
print(random.randrange(0, 10, 5))  # 0 2 4 6 8 10


