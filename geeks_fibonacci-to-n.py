tc = int(input())

for count in range(0,tc,1):
    n=int(input())

    a=0
    b=1
    print(str(a)+' '+str(b),end=' ')
    while b<=n:
        print(a+b,end=' ')
        temp = a
        a = b
        b = temp + b

        if(a+b>n):
            break
    print()

    
        
