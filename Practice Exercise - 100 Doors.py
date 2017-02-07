list_doors=[]
n = 100

def ndoors(n):
    for i in range(1,n+1):
        if (i*i) <= n:
            list_doors.append(i*i)
    return(list_doors)
