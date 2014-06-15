def getNoRectangles(n):
    from math import sqrt
    res = 0
    for i in range(1, int(sqrt(n))+1):
        res += int(n/i)-i+1
    return res

N = int(input())
print (getNoRectangles(N))
