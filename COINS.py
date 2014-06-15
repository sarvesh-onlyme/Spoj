def getCurrency(n):
    n = int(n)
    if n in dp:
        return dp[n]
    else:
        dp[n] = max(n, getCurrency(n/2)+getCurrency(n/3)+getCurrency(n/4))
        return dp[n]

dp = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6}
res = []
t = 10
while(t):
    n = input()
    if n=="":
        break
    else:
        n = int(n)
    res.append(getCurrency(n))
    t -= 1

for r in res:
    print (r)
