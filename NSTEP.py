case = int(input())
res = []
no = [[0, 0, 0], [1, 1, 1], [2, 2, 0]]
def get_no(x, y):
    l = no.__len__()
    if(no[l-1][0] >= x+y):
        if(no[x+y][1] == x and no[x+y][2] == y):
            return no[x+y][0]
        elif(no[x+y-1][1] == x and no[x+y-1][2] == y):
            return no[x+y-1][0]
        else:
            return "No Number"
    temp = no[l-1][0]
    _x = no[l-1][1]
    _y = no[l-1][2]
    while(l <= x+y):
        temp +=1
        if(temp%4 == 0):
            _x -=1
            _y +=1
        elif(temp%4 == 2):
            _x, _y = _x+1, _y-1
        else:
            _x, _y = _x+1, _y+1
        no.append([temp, _x, _y])
        l +=1
    return get_no(x, y)

for i in range(case):
    a = input().split()
    res.append(get_no(int(a[0]), int(a[1])))
for r in res:
    print(r)
    
"""
0  0,0
1  1,1
2  2,0
3  3,1
4  2,2
5  3,3
6  4,2
7  5,3
8  4,4
9  5,5
"""

