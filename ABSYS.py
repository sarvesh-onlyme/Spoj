t = int(input())
res = []
while(t):
    s = input().split()
    if len(s)==0:
        continue
    if not s[4].isdigit():
        s[4] = str(int(s[0])+int(s[2]))
        res.append(" ".join(s))
    else:
        if s[0].isdigit():
            s[2] = str(int(s[4])-int(s[0]))
            res.append(" ".join(s))
        else:
            s[0] = str(int(s[4])-int(s[2]))
            res.append(" ".join(s))
    t -=1

for r in res:
    print(r)
