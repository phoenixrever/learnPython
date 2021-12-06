# coding: utf-8

str = "the quick brown fox jump over the lazy dog"
print(str)
print(str[0])
print(str[0:9])  # the quick[0,9)
print(str[:9])  # the quick[0,9)
print(str[0:9:2])  # teqik
print(str[10:])  # [10,~]

print(r"里面的\n\t\'转义全部不解释")
print(str.__len__())

# 首字母大写
print(str.capitalize())

# 总共100个*字符来居中
print(str.center(len(str) + 20, "="))  # ==========the quick brown fox jump over the lazy dog==========
# 左对齐字符串不够不指定默认填充空格
print(str.ljust(len(str) + 20, '*'))  # the quick brown fox jump over the lazy dog********************
print(str.rjust(len(str) + 20, '*'))  # ********************the quick brown fox jump over the lazy dog

# 返回从0到字符串长度字符串种 o 出现的次数
print(str.count('o', 0, len(str)))

# 易指定的格式编码字符串 出错爆valueError 异常 除非errors 指定的是 'ignore' 或者 'replace'
s = str.encode(encoding='utf-8', errors="strict")
# 解码  常用
print(s.decode(encoding='utf-8', errors="strict"))

# 字符串是否以指定的字符串为结尾 是的返回true
print(str.endswith("dog", 0, len(str)))

# 是否包含指定的字符串 包含返回找到的第一个索引 不包含返回-1
print(str.find("e", 0, len(str)))
# 从右边开始查找
print(str.rfind("e", 0, len(str)))

# 和上面一样区别在于没有回报异常
print(str.index("e", 0, len(str)))
# 从右边开始查找
print(str.rindex("e", 0, len(str)))

m = '123aa1a'
# 至少有一个字符 都为数字或字母  意味着字符串中不能有空格等其他字符
print(m.isalnum())
# 至少有一个字符 都为字母
print(m.isalpha())
# 至少有一个字符 纯数字
print(m.isdigit())
print(m.isnumeric())

n = "the world"
# 是否全是大写
print(n.isupper())
# 转成大写
print(n.upper())
# 是否全是小写
print(n.islower())
# 转成小写
print(n.lower())

# 分隔符作为join的主体
a = 'abc'
b = '*'
print(b.join(a))  # a*b*c

toStrip = "****hello****"
# 截掉字符串左边字符不指定默认空格
print(toStrip.lstrip("*"))  # hello****
print(toStrip.rstrip("*"))  # ****hello

print(max(str))  # z
print(min(str))  # 最小的是空格 这里看不出来

# 最后一个参数指定替换参数
y = "xxxxx"
print(y.replace("x", ">", 3))

# #TODO 不懂
# s = 'o o oo ooo oo ooo'
# print(s.maketrans('o', '>'))
# print(s)

#后面的参数代表截取的数组的总长度
print(str.split(' ', 3))


