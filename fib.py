list = [ x for x in range(1,100)]
fib = (list[n - 1] + list[n - 2] for n in list if n >= 2)
for val in fib:
    print(val)