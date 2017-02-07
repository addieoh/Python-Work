poly = [0,5,1,4]

if poly == []:
    print([])
else:
    x = 0
    z = []
    for i in poly:
        x = ((i) * poly.index(i))
        z.append(x)
    del(z[0])
    print (z)





