N = int(input())
res = []
for i in range(N):
    t = 0
    sum = 0
    input()
    children = int(input())
    for j in range(children):
        a = int(input())
        sum += a
    if sum%children == 0:
        res.append('YES')
    else:
        res.append('NO')
for r in res:
    print(r)
