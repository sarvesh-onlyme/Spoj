res = []

def no_apples(apples, diff):
    if (apples%2 == 0):
        klaudia = int(apples//2 + diff//2)
        return klaudia
    return 1 + no_apples(apples-1, diff-1)

for i in range(10):
    apples = int(input())
    diff = int(input())
    klaudia = no_apples(apples, diff)
    res.append(klaudia)
    res.append(apples-klaudia)
    
for r in res:
    print(r)

