tc = int(input())

def sort(arr,n):
    for i in range(0,n,1):
        for j in range(0,n-1-i,1):
            if arr[j+1]<arr[j]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    return arr

for count in range(0,tc,1):
    n = int(input())
    #flag = 0

    arr = [int(x) for x in input().split()]
    arrset = set(arr)

    '''for i in range(0,n,1):
        if i==0:
            flag+=1
            pos = arr[i]
        elif arr[i]==pos:
            continue
        else:
            flag+=1
            pos = arr[i]'''

    print(len(arrset))
