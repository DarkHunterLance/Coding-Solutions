tc = int(input())

for count in range(0,tc,1):

    countnum=0
    
    n= int(input())

    arr = [int(x) for x in input().split()]

    k = int(input())

    for i in range(0,n,1):
        if arr[i]<=k:
            countnum+=1
        else:
            continue
    print(countnum)
