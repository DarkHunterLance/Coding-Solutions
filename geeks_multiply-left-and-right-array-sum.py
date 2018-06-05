tc = int(input())

for count in range(0,tc,1):
    n = int(input())

    list1 = []
    list2 = []
    sum1 = 0
    sum2 = 0

    orr = [int(x) for x in input().split()]

    for i in range(0,int(n/2),1):
        list1.append(orr[i])
    for i in range(int(n/2),n,1):
        list2.append(orr[i])

    sum1 = sum(list1)
    sum2 = sum(list2)

    print(sum1*sum2)
