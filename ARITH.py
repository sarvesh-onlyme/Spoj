def addition(digit1, digit2):
    #For string addition
    #maxLen = max(len(digit1), len(digit2))
    #d1 = digit1.zfill(maxLen)
    #d2 = digit2.zfill(maxLen)
    #add = ''
    #carry = 0 
    #for i in range(maxLen-1, -1, -1):
    #    temp = int(d1[i]) + int(d2[i]) + carry
    #    carry = int(temp/10)
    #    add = str(temp%10) + add
    #if carry:
    #    add = '1' + add
    add = str(int(digit1)+int(digit2))
    digit2 = '+' + digit2
    maxLen = max(len(add), len(digit2))
    digit1 = digit1.rjust(maxLen)
    digit2 = digit2.rjust(maxLen)
    add = add.rjust(maxLen)
    print (digit1)
    print (digit2)
    print ('-'*maxLen)
    print (add)

def substraction(digit1, digit2):
    #Assuming digit2<=digit1
    #maxLen = len(digit1)
    #d1 = digit1
    #d2 = digit2.zfill(maxLen)
    #sub = ''
    #borrow = 0
    #for i in range(maxLen-1, -1, -1):
    #    temp = int(d1[i])-borrow - int(d2[i])
    #    if temp<0:
    #        temp += 10
    #        borrow = 1
    #    else:
    #        borrow = 0
    #    sub = str(temp) + sub
    sub = str(int(digit1)-int(digit2))
    digit2 = '-' + digit2
    maxLen = max(len(digit1), len(digit2))
    dashLen = max(len(digit2), len(sub))
    digit1 = digit1.rjust(maxLen)
    digit2 = digit2.rjust(maxLen)
    #sub = ''.join([s.lstrip('0') for s in sub])
    sub = sub.rjust(maxLen)
    print (digit1)
    print (digit2)
    print (('-'*dashLen).rjust(maxLen))
    print (sub)

def multiplication(digit1, digit2):
    len1, len2 = len(digit1), len(digit2)
    maxLen = max(len1, len2)
    digitMul = []
    Max = 0
    for i in range(len2-1, -1, -1):
        temp = ''
        carry = 0
        if digit2[i]=='0':
            digitMul.append('0')
        else:
            #for j in range(len1-1, -1, -1):
            #    m = int(digit2[i])*int(digit1[j]) + carry
            #    temp = str(m%10) + temp
            #    carry = int(m/10)
            #if carry:
            #    temp = '1' + temp
            #digitMul.append(temp)
            digitMul.append(str(int(digit1)*int(digit2[i])))
    add = 0
    for i in range(len2):
        add = add + int(digitMul[i]+'0'*i)
        digitMul[i] = digitMul[i].ljust(len(digitMul[i])+i)
    add = str(add)
    addLen = max(len(add), len1, len2+1)
    print(digit1.rjust(addLen))
    print(('*'+digit2).rjust(addLen))
    print(('-'*max(len2+1, len(digitMul[0]))).rjust(addLen))
    for i in range(len2):
        print (digitMul[i].rjust(addLen))
    if len2 == 1:
        return
    if digit2 == '0':
        print('--'.rjust(addLen))
    elif digit1 == '0':
        print(('-'*len2).rjust(addLen))
    else:
        print(('-'*len(add)).rjust(addLen))
    print(add.rjust(addLen))


def arith(string):
    if string.find('+') != -1:
        digit1, digit2 = string.split('+')
        addition(digit1, digit2)
    elif string.find('-') != -1:
        digit1, digit2 = string.split('-')
        substraction(digit1, digit2)
    else:
        digit1, digit2 = string.split('*')
        multiplication(digit1, digit2)

t = int(input())
string = []
for i in range(t):
    string.append(input())
for i in string:
    arith(i)
    print ("")
