"""
输入一个数判断其是否为素数？
如果判断是素数？-> 能被 1 和自身整除为素数
"""
number = int(input('integer = '))

for i in range(2,number-1):# 不考虑 1和自身
    check = number % i
    if(check == 0):
        break
if(check == 0):
    print('不是素数')
else:
    print('是素数')
