def LCSLength(X, Y):
    C = []
    m = X.__len__()
    n = Y.__len__()
    C = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if (X[i-1] == Y[j-1]):
                C[j][i] = C[j-1][i-1]+1
            else:
                C[j][i] = max(C[j-1][i], C[j][i-1])
    return C[n][m]

result = []
case = int(input())
for i in range(case):
    she = input().split()
    she.pop()
    he = []
    a = input()
    while(a != '0'):
        he.append(a.split())
        a = input()
    maxim = 0
    for j in he:
        j.pop()
        s = LCSLength(she, j)
        if s > maxim:
            maxim = s
    result.append(maxim)
for i in result:
    print (i)

