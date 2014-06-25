t = int(input())
while(t):
    tmp = input()
    if tmp == "":
        continue
    #NG, NM = list(map(int, tmp.split()))
    NGStrength = list(map(int, input().split()))
    NMStrength = list(map(int, input().split()))
    if max(NGStrength) >= max(NMStrength):
        print ("Godzilla")
    else:
        print("MechaGodzilla")
    t -= 1
