case = int(input())
res = []

def candy(a, total):
    a.sort()
    a.reverse()
    l = a.__len__()
    avg = int(total/l)
    i, j = 0, l-1
    moves = 0
    while(i != j):
        give = a[i] - avg
        take = avg - a[j]
        if(give >= take):
            a[i] -= take
            a[j] +=take
            j -=1
            moves +=take
        else:
            a[i] -= give
            a[j] += give
            i +=1
            moves += give
    return moves
while(case != -1):
    a = []
    total = 0
    for i in range(case):
        k = int(input())
        a.append(k)
        total +=k
    if(total/case != int(total/case)):
        res.append(-1)
        case = int(input())
        continue
    res.append(candy(a, total))
    case = int(input())
for r in res:
    print(r)

