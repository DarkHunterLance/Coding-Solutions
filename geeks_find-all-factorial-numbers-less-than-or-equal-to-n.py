tc = int(input())

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)

for count in range(0,tc,1):
    n = int(input())

    for i in range(1,n+1,1):
        res = fact(i)
        if(res<=n):
            print(res,end=' ')
        else:
            break

    print()
