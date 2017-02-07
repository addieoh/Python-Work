p_d = 13

ac = 0
x = (p_d - 1)//2
for i in range(-x,x+1):
    for j in range(-x,x+1):
        dist = ((i**2)+(j**2))**0.5
        if dist <= (p_d/2):
            ac += 1
print (4*ac/(p_d**2))
