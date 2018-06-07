tc = int(input())

for count in range(0,tc,1):
    n = int(input())

    x = [int(x) for x in input().split()]

    res = sum(x)

    if res%2==0:
        print("2")
    else:
        print("1")
