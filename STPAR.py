def stpar(n, mobile):
    t = 1
    stack = [n+1]
    stackLen = 1
    stackMin = n+1
    while t<n:
        if stack[stackLen-1] == t:
            stack.pop()
            stackLen -= 1
            t +=1
            stackMin = stack[stackLen-1]
            continue
        tmp = mobile.pop(0)
        if tmp == t:
            t += 1       
        else:
            if stackMin > tmp:
                stack.append(tmp)
                stackLen += 1
                stackMin = tmp
            else:
                print("no")
                return
    print("yes")
    return

n = int(input())
while(n):
    mobile = list(map(int, input().split()))
    stpar(n, mobile)
    n = int(input())
