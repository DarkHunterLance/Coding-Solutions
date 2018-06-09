tc = int(input())

for count in range(0,tc,1):
    inputval = [int(x) for x in input().split()]
    n = inputval[0]
    k = inputval[1]

    list1 = []
    list2 = []

    while n>0:
        r = n%k
        list1.append(r)
        n = int(n/k)

    for i in range(0,len(list1),1):
        list2.append(list1[len(list1)-1-i])

    print(''.join(str(e) for e in list2))

    
