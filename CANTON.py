case = int(input())
res = []
diagonal = [1, 2, 4]
diff = 3
def get_index(n):
    global diff
    last = diagonal[diagonal.__len__()-1]
    if last <= n:
        while(last <= n):
            last = last+diff
            diff +=1
            diagonal.append(last)
    i, j = 0, 0
    while(n >= diagonal[i]):
        i +=1
    i -=1
    temp = i
    d = n - diagonal[i]
    i -=d
    j +=d
    if(temp%2 == 0):
        i, j = j, i
    return i+1, j+1

for i in range(case):
    n = int(input())
    res.append([n, get_index(n)])
for r in res:
    print("TERM %d IS %d/%d"%(r[0], r[1][1], r[1][0]))

