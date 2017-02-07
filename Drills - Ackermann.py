import sys
sys.setrecursionlimit(100000)

def ack(m,n):
    if m == 0:
        return (n + 1, 1)
    elif m > 0 and n == 0:
        a, cnt = ack(m - 1.0, 1.0)
        return a, cnt+1
    elif m > 0 and n > 0:
        a1, cnt1 = ack(m, n - 1.0)
        a2, cnt2 = ack(m - 1.0, a1)
        return a2, 1 + cnt1 + cnt2

print (ack(3,9))
