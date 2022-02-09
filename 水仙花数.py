for num in range(100,1000):
    low = num % 10 #整除 10之后的余数
    mid = num // 10 % 10
    high = num // 100 % 10
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)