from math import pi
n = int(input())
while(n):
    print (format(round(n*n/(2*pi), 2), '.2f'))
    n = int(input())
