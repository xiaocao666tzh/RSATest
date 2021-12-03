e = int(input('请输入公钥\n'))
n=int(input('请输入两质数积\n'))
m = int(input('请输入明文\n'))
c = pow(m,e)
c = c % n
print('密文是',c)
