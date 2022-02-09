"""
分段函数求值
		3x - 5	(x > 1)
f(x) =	x + 2	(-1 <= x <= 1)
		5x + 3	(x < -1)
"""
x = float(input('x = '))
if(x > 1):
    x = 3 * x - 5
elif x <= 1 and x >= -1:
    if x <= 1:
        x = x + 2
    else:
        x = 5 * x + 3
print(x)