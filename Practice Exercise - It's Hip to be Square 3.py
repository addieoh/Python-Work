x = 16

def perfect_square(x):
    if x > 1:
        for i in range (2,x):
            if (i * i) == x:
                return(True)
        else:
            return (False)
    else:
        return (True)


print(perfect_square(x))
