t=int(input())
exp=[]
for i in range(0, t):
    exp.append(input())
for i in range(0, t):
    stack=[]
    for j in exp[i]:
        if(j=='('):
            stack.append(j)
            continue
        elif(j==')'):
            k=stack.pop()
            while(k!='('):
                print(k, end="")
                k=stack.pop()
            continue
        elif(j=='+' or j=='-' or j=='*' or j=='/' or j=='^'):
            stack.append(j)
        else:
            print(j, end="")
    print("")
