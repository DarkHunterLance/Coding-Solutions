tc = int(input())

for count in range(0,tc,1):
    n = int(input())

    list1 = [x for x in input().split()]

    res = ''.join(str(e) for e in list1)

    print(res)
