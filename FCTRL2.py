case = int(input())
fact = [1, 1, 2, 6]
result = []
for i in range(case):
    k = int(input())
    if k < fact.__len__():
        result.append(fact[k])
        continue
    l = fact.__len__()
    while(l <= k+1):
        fact.append(fact[l-1]*l)
        l +=1
    result.append(fact[k])
for r in result:
    print(r)

