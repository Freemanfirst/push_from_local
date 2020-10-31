# greatest common divisor
# 欧几里得算法
def gcd(a,b):
    if a<b:
        a,b=b,a
    while b!=0:
        a,b=b,a%b
    return a