tc = int(input())

for count in range(0,tc,1):
    n = int(input())
    flag = 0

    for i in range(1,n+1,1):
        temp = str(i)
        list1 = list(temp)

        if '0' in list1:
            flag = flag+1

    print(flag)
