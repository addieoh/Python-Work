d = {'k1':'cat', 'k2':'dog'}
k1, k2 = d.keys()

def swap(d, k1, k2):
    d[k1], d[k2] = d[k2], d[k1]
    return d

print(swap(d, k1, k2))


