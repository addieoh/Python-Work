x = 5
f = x + 2
g = 3 * x

def f(x):
    return x + 2

def g(x):
    return 3 * x

def composite_result(f, g, x):
    return f(g(x))

print (composite_result(f, g, x))
