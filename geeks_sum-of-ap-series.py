tc = int(input())

for count in range(0,tc,1):
    [a,d,n] = [float(x) for x in input().split()]
    res = 0.5*n*(2*a + (n-1)*d)

    print(round(res,2))
