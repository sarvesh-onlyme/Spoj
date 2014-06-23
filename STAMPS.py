t = int(input())
for i in range(t):
    stamps, friends = input().split()
    stamps, friends = int(stamps), int(friends)
    offering = list(map(int, input().split()))
    offering.sort()
    sum = 0
    t = friends
    while t and sum<stamps:
        sum += int(offering.pop())
        t -= 1
    if sum < stamps:
        print("Scenario #"+str(i+1)+":")
        print ("impossible")
    else:
        print ("Scenario #"+str(i+1)+":")
        print(friends-t)
