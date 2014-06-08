a = int(input())
res = []

def decode(word, a):
    dec = ''
    d1 = a*2-1
    d2 = 1
    temp = 0
    while(temp < a):
        i = temp
        d = d1
        while(1):
            try:
                dec += word[i]
                i +=d
                if(d == d1):
                    d=d2
                else:
                    d = d1
            except:
                break
        d1 -= 2
        d2 +=2
        temp +=1
    return dec

while(a):
    word = input()
    res.append(decode(word, a))
    a = int(input())
for r in res:
    print (r)

