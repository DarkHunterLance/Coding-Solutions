import math
tc = int(input())

for count in range(0,tc,1):
    s = input()
    res = 0

    list1 = list(s)

    for i in range(0,len(list1),1):
        res = res + ord(list1[i])

    sq = math.sqrt(res)

    if (sq-int(sq))==0:
        print('1')
    else:
        print('0')
