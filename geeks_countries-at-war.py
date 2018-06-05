tc = int(input())

for count in range(0,tc,1):
    n= int(input())
    count1=0
    count2=0

    a = [int(x) for x in input().split()]
    b = [int(y) for y in input().split()]

    for i in range(0,n,1):
        if a[i]>b[i]:
            count1+=1
        elif a[i]<b[i]:
            count2+=1
        else:
            continue

    print(str(count1)+' '+str(count2),end=' ')

    if count1>count2:
        print('A')
    elif count1<count2:
        print('B')
    else:
        print('DRAW')
