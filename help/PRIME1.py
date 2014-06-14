import timeit
start = timeit.default_timer()
prime = [2, 3, 5, 7]
lenPrime = 4
t = int(input())
inp = []
for i in range(t):
    inp.append(input().split())

for i in range(t):
    if int(inp[i][1]) <= prime[lenPrime-1]:
        continue
    while (int(inp[i][1]) > prime[lenPrime-1]):
        p = prime[lenPrime-1]+2
        append = 0
        while not append:
            canPrime = 0
            for j in prime:
                if p%j == 0:
                    p +=2
                    canPrime = 0
                    break
                else:
                    canPrime = 1
            if canPrime:
                prime.append(p)
                append = 1
                lenPrime += 1

for i in range(t):
    output = [p for p in prime if p>=int(inp[i][0]) and p<= int(inp[i][1])]
    for i in output:
        print (i)
    print ("")
