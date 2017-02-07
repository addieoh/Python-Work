def dictmap(d, f):
    for k in d:
        x = d[k]
        d[k] = f(x)
    return d

