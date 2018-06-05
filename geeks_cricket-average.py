tc = int(input())

for count in range(0,tc,1):
    n = int(input())
    flag = 0
    res = 0

    for i in range(0,n,1):
        temp = [str(x) for x in input().split()]
        res = res + int(temp[0])

        if temp[1]=='out':
            flag+= 1

    if flag==0:
        print('-1')
    else:
        if ((res/flag)-int(res/flag))==0:
            print(int(res/flag))
        else:
            print(int(res/flag)+1)
        
        
