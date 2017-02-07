poly = [3,7,9]
const = 0.69

if poly == []:
    print([const])
else:
    x = 0
    z = []
    for i in poly:
        x = ((i) / (poly.index(i)+1))
        z.append(x)
    print([const]+z)
