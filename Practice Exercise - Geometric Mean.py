numbers = [2, 7, 3, 9, 13]

if len(numbers) == 0:
    print("None")
else:
    p = 1
    for i in numbers:
        p *= i
    print (p ** (1/len(numbers)))
