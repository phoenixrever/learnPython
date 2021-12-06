# coding: utf-8

def myFunvtion(arg):
    print("hello %s" % arg)


myFunvtion("nevermore")


def add(m, n):
    return m + n


print(add(1, 2))


# 返回多个值
def multiReturn(m, n):
    return m, n


print(multiReturn(1, 2))  # (1, 2)
a, b = multiReturn(1, 2)
print(a, end='\t')
print(b)
