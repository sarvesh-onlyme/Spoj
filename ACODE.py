a = input()
res = []

def decoding(a):
    l = a.__len__()
    dp = [1] + [0]*(l-1)
    if(l>1):
        if(int(a[1])):
            dp[1] +=dp[0]
        if(int(a[0]+a[1])>9 and int(a[0] + a[1])<=26):
            dp[1] += dp[0]
    for i in range(2, l):
        if(int(a[i])):
            dp[i] +=dp[i-1]
        if(int(a[i-1]+a[i])> 9 and int(a[i-1]+a[i])<=26):
            dp[i] += dp[i-2]
    return dp[l-1]

while(int(a)):
    res.append(decoding(a))
    a = input()
for r in res:
    print(r)

