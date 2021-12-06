# coding: utf-8

print("#==========================list========================")
list = ["123", 22, 3.1400]
list2 = ["456"]
print(list)
# 从0开始  第二个参数从哪结束  第三个参数每隔几个数字取
print(list[0:list.__len__():1])
# 拼接list
print(list + list2)
# 拼接list
list.extend(["55", "22333"])
# 插入
list.insert(0, "0000")
print(list)
# append 直接加载数组末尾
list2.append("push")
# 注意直接增加列表的话会是子list ['456', 'push', ['son', 'list']]
list2.append(["son", "list"])
print(list2)
# 可以指定pop那个元素
print("===============删除=============")
list2.pop(0)
del list2[0]
# 重复数据的删除找到的第一个
list2.remove(["son", "list"])
print(list2)

print(list)
# 包含
print(list.__contains__(22));
if 11 in list2:
    print("11 in 22")
print(22 in list)
print(22 not in list)
print(list)
# 123 在数组的1到4(不包含4  左闭右开[1,4))的位置上有没出现 出现返回索引 没有报错
# print(list.index(22,3,4))

# ==========================统计元素出现次数============
list.extend(["123", "123"])
print(list)
print(list.count("123"))

number = [2, 4, 5, 2, 5, 3, ]
number.sort(reverse=True)
print(number)
# for i in list:
#     print(i)
# for i in range(0, len(list), 1):
#     print(list[i])
