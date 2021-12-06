# coding: utf-8
from typing import io

if True:
    print('非0非空值都为true')
else:
    print('0 None 为false')

print("end")

score = 87

if score > 90:
    print('excellent')
else:
    if score < 90 and score > 80:
        print('good')
    else:
        print('bad boy')

score = 50

if score > 90:
    print('excellent')
if 80 <= score <= 90:
    print('good')
else:
    if 60 < score < 70:
        print('bad boy')
    print('you are a looser')

if 80 <= score <= 90:
    print('good')
elif 70 < score < 80:
    print('not bad')
elif 60 < score < 70:
    print('not bad')
else:
    print('not bad')
# ===========for==========
for i in range(5):
    print(i)  # 0 1 2 3 4
print('-----------')

# int i=0;i<10;i+=2
for i in range(0, 10, 2):
    print(i)

name = 'the hot dog sell a fox'
for s in name:
    print(s, end='\t')

array = ['a', 'b', 'c', 'd']
print()
for a in array:
    print(a, end='\t')

print()
for i in range(len(array)):
    print(i, array[i], end='\t\t')

print('\n================while=============')
c = 3
while c >= 0:
    print(c, end='\t')
    c -= 1  # 没有c--

# 1　到100 求和
print('\n======到100 求和========')
n = 1
m = 0
while n <= 100:
    m = m + n
    n += 1
print(m)

# 注意range函数stop 不包含等于
s = 0
for i in range(1, 101, 1):
    s += i
print(s)

print('\n===================')
count = 0
while count < 5:
    count += 1
else:
    print('count:%d' % count)

print('\n=======break continue pass============')
count = 0
while count < 100:
    count += 1
    if count == 10:
        break
print('break---count:%d' % count)

for i in range(0, 10, 1):
    if i == 3 or i == 4 or i == 5 or i == 6:
        continue
    if i == 7 or i == 8:
        pass  # 啥都不做不知道啥用估计和空函数差不多
    print(i, end='\t')
