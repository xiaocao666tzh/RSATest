import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def coprime(a, b):
    return gcd(a, b) == 1


# 两个函数作用均为判断两数是否互质

p = 0
q = 0
while p == q:
    p = random.choice([2, 3, 5, 7, 11, 13, 17, 19])
    q = random.choice([2, 3, 5, 7, 11, 13, 17, 19])
n = p * q
n1 = (p - 1) * (q - 1)

# 随机取p和q（此处只取20以内的质数方便计算，并计算出n以及φ(n)
while True:
    e = random.randint(1, n1)
    if coprime(e, n1):
        break
for i in range(1, 10000):
    d = (i * n1 + 1) / e
    if e*d > n1:
        if d % 1 == 0:
            d = int(d)
            break
print('公钥是',e)
print('两质数积为',n)
# 计算出公钥以及私钥


c = int(input('请输入密文\n'))
m = pow(c,d)
m = m % n
print('明文是',m)