    # coding: utf-8
tuple = ("123", 456, 7.89, ["123", 456])
print(tuple)
# 元祖里面的对象不可改变,但是里面的元素的子元素可改变
tuple[3][0] = "456"
print(tuple)
# 定义只有1个元素的 元祖必须加,
print((1,))
# 删除整个元祖变量
del tuple;

# =============================字典 dict==============================
d = {"123": 456, " 7.89": 789, "son": ["123", 456]}
print(d)

# 找不到报错
# print(d["445"])
# 找不到 返回none 如果设置了第二个参数 返回设置的值
print(d.get("445", "12222"))
print(d.keys())
print(d.values())
print(d.items())
print("==============for===============")
for key, value in d.items():
    print("key:%s value:%s" % (key, value))

a = ["a", "b", 'c', 'd', 'e']

for i in range(0, len(a), 1):
    print(a[i])

# 转成键值对形式 key:0 value:a
for k, v in enumerate(a):
    print("key:%s value:%s" % (k, v))
print("==============for===============")
del d["123"]
print(d)
d.clear();
print(d)
# 删除变量
del d

# 其他类型转成字典 必须要是键值对
list = [(12, 2), (22, 33)]
list2 = [[132, 32], [2342, 433]]
print(dict(list))
print(dict(list2))

d1 = {12: 2, 22: 33}
d2 = {132: 32, 2342: 433}
# 合并字典
d1.update(d2)
print(d1)

l1 = [1, 2, 3, 4]
l2 = [4, 5, 6, 9, ]
# 2个列表转自字典 {1: 4, 2: 5, 3: 6, 4: 9}
print(dict(zip(l1, l2)))

# 集合 set
s = set([1, 2, 2, 3])
print(s)
