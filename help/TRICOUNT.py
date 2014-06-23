def countTriangles(n):
    if n%2 == 0:
        triangle = (n*(n+2)*((2*n)+1))/8
    else:
        triangle = ((n*(n+2)*((2*n)+1))-1)/8
    return int(triangle)

t = int(input())
res = []
for i in range(t):
    n = int(input())
    res.append(countTriangles(n))

for r in res:
    print(r)
