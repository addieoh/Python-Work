def hailstone_sequence(a_0):
    x = [a_0]
    while a_0 > 1:
        if a_0 % 2 == 0:
            a_0 = (a_0 // 2)
            x.append(a_0)
        elif a_0 > 1:
            a_0 = (3 * a_0 + 1)
            x.append(a_0)
    return x
