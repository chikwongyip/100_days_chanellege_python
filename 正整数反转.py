num = int(input('x = '))
num_dig = 0
while ( num // 10) > 10:
    num_dig = num_dig + 1

for i in range(0,num_dig):
    ex_num = ex_num + (num % 10 * (10 ** num_dig - i))

print(ex_num)