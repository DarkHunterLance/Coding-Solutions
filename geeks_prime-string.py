import math

tc = int(input())

def ascsum(string):
    list1 = list(string)
    res=0

    for i in range(0,len(list1),1):
        res = res + ord(list1[i])
    return res


def prime(n):

    if n==0 or n==1:
        return False
    elif n==2:
        return True
    else:
        for i in range(2,int(math.sqrt(n)+1),1):
            if n%i==0:
                return False
            else:
                continue
        return True

for count in range(0,tc,1):
    n = int(input())

    string = input()

    sumlen = ascsum(string)

    x = prime(sumlen)

    if x==True:
        print('YES')
    else:
        print('NO')
