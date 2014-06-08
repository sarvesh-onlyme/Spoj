case = int(input())
result = []
for i in range(case):
    a = input()
    b, c = a.split()
    b = b[::-1]
    c = c[::-1]
    r = int(b) + int(c)
    r = repr(r)[::-1]
    r = int(r)
    result.append(r)
for i in result:
    print (i)

