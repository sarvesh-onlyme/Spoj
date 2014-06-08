case = int(input())
res = []
for i in range(case):
    n = int(input())
    men = [ int(i) for i in input().split()]
    men.sort()
    women = [int(i) for i in input().split()]
    women.sort()
    r = 0
    for i in range(n):
        r += men[i]*women[i]
    res.append(r)
for r in res:
    print (r)

