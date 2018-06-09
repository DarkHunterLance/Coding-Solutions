import math
tc = int(input())

for count in range(0,tc,1):
    [n,k] = [int(x) for x in input().split()]

    for flag in range(0,n,1):
        if flag==0:
            res=1
        else:
            res = res * k


    print(math.fmod(res,(10**9+7)))
