tc = int(input())

for count in range(0,tc,1):
    n = int(input())
    temp = list(str(n))
    reqlen = len(temp)

    res = (n*n*n)
    #print(res,end=':')

    list1 = list(str(res))
    #print(list1,end=':')

    val = res%(10**(reqlen))
    #print(val,end=':')

    if val == n:
        print('1')
    else:
        print('0')
