import sys
# 生成式
f = [x for x in range(1,10)]
print(f)
print('\n')
f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)
print('\n')
f = [x ** 2 for x in range(1,1000)]
print(sys.getsizeof(f))
print(f)
#生成器
#生成器不占用内存
f = (x ** 2 for x in range(1,1000))
print(sys.getsizeof(f))
print('\n')
for val in f:
    print(val)