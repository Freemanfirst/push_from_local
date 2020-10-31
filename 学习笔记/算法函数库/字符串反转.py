# f1 反转列表法

a = 'abcdef'
b = list(a)
b.reverse()
b = ''.join(b)
print(b)

# f2 循环反向迭代法

a = 'abcdef'
b = ''
for i in a:
	b = i + b
print(b)

# f3 反向循环迭代法
a = 'abcdef'
b = ''
for i in a[::-1]:
	b = b + i 
print(b)

# f4 倒序切片法
a = 'abcdef'
b = a[::-1]
print(b)

# f5 遍历索引法
a = 'abcdef'
b = ''
for i in range(1,len(a)+1):
	b = b + a[-i]
print(b)

# f6 列表弹出法
a = 'abcdef'
a = list(a)
b = ''
while len(a) > 0:
	b = b + a.pop()
print(b)

# f7 列表解析式法
a = 'abcdef'
b = ''.join(i for i in a[::-1])
print(b)

# f8 反向遍历索引法
a = 'abcdef'
b = ''
for i in range(len(a)-1,-1,-1):
	b = b + a[i]
print(b)

# f9 累积相加法
a = 'abcdef'
from functools import reduce
def f(x,y):
	return y + x
b = reduce(f,a)
print(b)

# f10 匿名函数法
a = 'abcdef'
b = reduce(lambda x,y:y+x,a)
print(b)

# f11 一维数组索引法
a = 'abcdef'
import pandas as pd 
b = pd.Series(list(a))
b = ''.join(b[::-1])
print(b)