numbers = [2, 7, 3, 9, 13]

if len(numbers) == 0:
    print("None")
else:
    p = 0
    for i in numbers:
        p += i
    print (p / len(numbers))
