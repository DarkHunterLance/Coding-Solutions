tc = int(input())

for count in range(0,tc,1):
    n1 = int(input())

    arr1 = [int(x) for x in input().split()]

    n2 = int(input())

    arr2 = [int(y) for y in input().split()]

    print(max(arr1)*min(arr2))
    
