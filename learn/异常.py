# coding: utf-8
d = [1, 2, 3, 4, 5]
try:
    d.remove(6)
except Exception as e:
    print("出了异常:", e)
