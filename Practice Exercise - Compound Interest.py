interest_rate = 1

if interest_rate == 0:
    print ("NEVER")
else:
    t = 0
    while (1 + interest_rate) ** t < 2:
        t = t + 1
    print (t)
