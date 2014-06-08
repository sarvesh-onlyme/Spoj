case = int(input())
res = []

def get_index(st):
    s = st
    temp = st
    for i in range(s.__len__()):
        if temp > s:
            temp = s
        s = s[-1:]+s[:-1]
    return (st+st).find(temp)+1

for i in range(case):
    st = input()
    res.append(get_index(st))
for r in res:
    print(r)

