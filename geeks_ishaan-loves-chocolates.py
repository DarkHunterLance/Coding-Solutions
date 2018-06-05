tc = int(input())

for count in range(0,tc,1):
    n = int(input())

    arr = [int(x) for x in input().split()]

    while(len(arr)!=1):
        if arr[0]>arr[len(arr)-1]:
            arr.remove(arr[0])
        elif arr[0]<=arr[len(arr)-1]:
            arr.remove(arr[len(arr)-1])

    for i in arr:
        print(i)
