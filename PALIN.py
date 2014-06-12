def palindrome(k):
    kLen = len(k)
    odd = kLen%2
    if odd:
        middle = k[int(kLen/2)]
    else:
        middle = ''
    left = k[:int(kLen/2)]
    right = left[::-1]
    pdrome = left + middle + right
    if pdrome > k:
        return pdrome
    else:
        if middle:
            if middle < '9':
                middle = str(int(middle)+1)
                return left+middle+right
            else:
                middle = '0'
        if left == len(left)*'9':
            return '1'+(kLen-1)*'0'+'1'
        else:
            #increse left
            leftList = list(left)
            last = len(left)-1
            while leftList[last]=='9':
                leftList[last] = '0'
                last -=1
            leftList[last] = str(int(leftList[last])+1)
            left = "".join(leftList)
            return left + middle + left[::-1]

t = int(input())
palin = []
for i in range(t):
    k = input()
    palin.append(palindrome(k))
for i in palin:
    print (i)
