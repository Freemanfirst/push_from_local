# 斐波那契数列（Fibonacci sequence），又称黄金分割数列
# 因数学家列昂纳多·斐波那契（Leonardoda Fibonacci）以兔子繁殖为例子而引入，故又称为“兔子数列”
# 指的是这样一个数列：1、1、2、3、5、8、13、21、34、......
# 在数学上，斐波纳契数列以如下被以递归的方法定义：F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=2，n∈N*）
# 斐波那契数列，难点在于算法，还有如果变成生成器，generator，就要用for循环去遍历可迭代的generator

# f1 递归法
def fib_recur(n):
	assert n>=0,"n>=0"
	if n<=1:
		return n
	return fib_recur(n-1) + fib_recur(n-2)

for i in range(1,20):
    print(fib_recur(i), end=' ')

# 写法最简洁，但是效率最低，会出现大量的重复计算，时间复杂度O(1.618^n)，而且最深度1000

# f2 递推法
def fib_loop(n):
	a,b = 0, 1
	for i in range(n):
		a,b = b, a+b
	return a

for i in range(1,20):
    print(fib_loop(i), end=' ')

# 递推法，就是递增法，时间复杂度是O(n)，呈线性增长，如果数据量巨大，速度会越拖越慢

# f3 生成器
def fib_loop_while(max):
	a,b = 0,1
	while max>0:
		a,b = b,a+b
		max -= 1
		yield a 

for i in fib_loop_while(10):
    print(i)

# 带有yield的函数都被看成生成器，生成器是可迭代对象，且具备__iter__ 和 __next__方法， 可以遍历获取元素
# python要求迭代器本身也是可迭代的，所以我们还要为迭代器实现__iter__方法，
# 而__iter__方法要返回一个迭代器，迭代器自身正是一个迭代器，
# 所以迭代器的__iter__方法返回自身即可

# f4 类实现内部魔法方法
class Fibonacci(object):
    """斐波那契数列迭代器"""

    def __init__(self, n):
        """
        :param n:int 指 生成数列的个数
        """
        self.n = n
        # 保存当前生成到的数据列的第几个数据，生成器中性质，记录位置，下一个位置的数据
        self.current = 0
        # 两个初始值
        self.a = 0
        self.b = 1

    def __next__(self):
        """当使用next()函数调用时，就会获取下一个数"""
        if self.current < self.n:
            self.a, self.b = self.b, self.a + self.b
            self.current += 1
            return self.a
        else:
            raise StopIteration

    def __iter__(self):
        """迭代器的__iter__ 返回自身即可"""
        return self


if __name__ == '__main__':
    fib = Fibonacci(15)
    for num in fib:
        print(num)

# for循环的本质是通过不断调用next()函数实现的
    for x in [1, 2, 3, 4, 5]:
        pass
# 相当于:
    # 首先获取可迭代对象
    it = iter([1, 2, 3, 4, 5])
    # while next
    while True:
        try:
            next(it)
        except StopIteration:
            # 遇到StopIteration就退出循环
            break

# f5 矩阵快速幂
import numpy as np

### 1
def fib_matrix(n):
    for i in range(n):
        res = pow((np.matrix([[1, 1], [1, 0]], dtype='int64')), i) * np.matrix([[1], [0]])
        print(int(res[0][0]))


# 调用
> fib_matrix(50)

### 2
# 使用矩阵计算斐波那契数列
def Fibonacci_Matrix_tool(n):
    Matrix = np.matrix("1 1;1 0", dtype='int64')
    # 返回是matrix类型
    return np.linalg.matrix_power(Matrix, n)

def Fibonacci_Matrix(n):
    result_list = []
    for i in range(0, n):
        result_list.append(np.array(Fibonacci_Matrix_tool(i))[0][0])
    return result_list

# 调用
> Fibonacci_Matrix(50)

### pow 速度 比 双**号快, np.linalg.matrix_power也是一种方法

# 因为幂运算可以使用二分加速，所以矩阵法的时间复杂度为 O(log n)
# 用科学计算包numpy来实现矩阵法 O(log n)