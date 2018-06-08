tc = int(input())

for count in range(0,tc,1):
    flag = 0
    x = int(input())

    [a,b] = [int(y) for y in input().split()]

    if(a>=x and b>x):
        
        for i in range(a+1,b,1):
            temp = str(i)
            #print(temp,end = ' : ')
            list1 = list(temp)
            #print(list1)
            flag = flag + list1.count(str(x))
                    
    print(flag)
