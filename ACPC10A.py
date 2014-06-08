i = input()
i = i.split()
result=[]
while(i != ['0']*3):
    a, b, c = int(i[0]), int(i[1]), int(i[2])
    if(b-a == c-b):
        r = 'AP '+repr(2*c-b)
        result.append(r)
    else:
        r = 'GP '+ repr(c*int(c/b))
        result.append(r)
    i=input().split()
for i in result:
    print(i)

