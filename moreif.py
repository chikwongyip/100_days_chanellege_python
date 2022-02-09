x = int(input('请输入数值: '))
if(x > 1):
    x = 3 * x -5
elif x >= -1 and x <= 1:
    x = x + 2
else:
    x = 5 * x + 3 
print(x)
