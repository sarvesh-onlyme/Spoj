def findNo(k):
    if k%2 == 0:
        return 442 + int((k-1)/2)*500
    else:
        return 192 + int((k-1)/2)*500

t = int(input())
res = []
for i in range(t):
    k = int(input())
    res.append(findNo(k))

for r in res:
    print (r)
