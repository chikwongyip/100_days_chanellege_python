"""
输入三条边长，如果能构成三角形就计算其周长和面积
任意两边之和必定大于第三边
已知三边长度 三边之和 除以 2
"""
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b > c and a + c > b and b + c > a :
    print('周长为： %f' % a + b + c)
    print('面积为: %f' % (a + b + c) * 0.5)
else:
    print('不能构成')
