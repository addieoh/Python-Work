dividend = 10
divisor = 5

if dividend == divisor:
    print(1)
    print(0)   
else:
    n = 0
    while n*divisor <= dividend:
        n = n + 1
    print(n-1)
    print(dividend - (n-1)*divisor)
