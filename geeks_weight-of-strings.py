tc = int(input())

for count in range(0,tc,1):
    s1 = input()
    s2 = input()

    list1 = list(s1)
    list2 = list(s2)

    sum1=0
    sum2=0

    for i in range(0,len(list1),1):
        sum1 = sum1 + (ord(list1[i])-96)

    for i in range(0,len(list2),1):
        sum2 = sum2 + (ord(list2[i])-96)

    if sum1>sum2:
        print('1')
    elif sum1<sum2:
        print('2')
    else:
        print('equal')
