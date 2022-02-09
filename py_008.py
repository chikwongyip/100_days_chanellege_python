def fac(num):
    result = 1
    for n in range(1,num + 1):
        result *= n
    return result

m = int(input('M = '))
n = int(input('N = '))

print(fac(m) // fac(n) // fac(m - n))