x = 5
f = x + 2
g = 3 * x

def f(x):
    return x + 2

def g(x):
    return 3 * x

def composite(f,g):
    def sub(x):
        return f(g(x))
    return sub

