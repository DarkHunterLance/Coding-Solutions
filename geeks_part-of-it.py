tc = int(input())

for count in range(0,tc,1):
    n = int(input())

    i = 1
    list1 = []

    while(2*i+1)<=n:
        if(i<3) or (i>=3 and i%3!=0):
            list1.append(2*i+1)
        i=i+1

   # print(list1)
    if n in list1:
        print("Yes")
    else:
        print("No")
        
