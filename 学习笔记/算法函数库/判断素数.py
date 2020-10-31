#运用python的数学函数
import math

def isPrime(n):
	if n<=1:
		return False
	for i in range(2,int(math.sqrt(n))+1):
		if n%i==0:
			return False
	    return True

#单行程序扫描素数
from math import sqrt
N=100
[p for p in range(2,N) if 0 not in [p%d for d in range(2,int(sqrt(p))+1)]]

#不使用模块的两种方法
def isPrime(n):
	if n<=1:
		return False
	i=2
	while i*i<=n:
		if n%i==0:
			return False
		i=i+1
	return True

def isPrime(n):    
    if n <= 1:    
        return False   
    if n == 2:    
        return True   
    if n % 2 == 0:    
        return False   
    i = 3   
    while i * i <= n:    
        if n % i == 0:    
            return False   
        i += 2   
    return True 