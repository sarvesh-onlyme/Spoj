def findLast(a, b):
    a = a%10
    if b==0:
        return 1
    elif b==1:
        return a
    digits = {
        0: [1, [0]],
        1: [1, [1]],
        2: [4, [6, 2, 4, 8]],
        3: [4, [1, 3, 9, 7]],
        4: [2, [6, 4]],
        5: [1, [5]],
        6: [1, [6]],
        7: [4, [1, 7, 9, 3]],
        8: [4, [6, 8, 4, 2]],
        9: [2, [1, 9]],
    }
    res = digits[a][1][b%digits[a][0]]
    return res

t = int(input())
res = []
for i in range(t):
    a, b = input().split()
    a, b = int(a), int(b)
    res.append(findLast(a, b))

for r in res:
    print(r)
