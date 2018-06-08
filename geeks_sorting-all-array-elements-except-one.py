tc = int(input())

def sort(arr):
    for i in range(0,len(arr),1):
        for j in range(0,len(arr)-1-i,1):
            if int(arr[j+1])<int(arr[j]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    return arr

for count in range(0,tc,1):
    n = int(input())

    arr = [x for x in input().split()]
    k = int(input())

    list1 = arr[0:k:1] + arr[k+1::1]

    #print("BEFORE SORTING : ",list1)

    list1 = sort(list1)

    list1.insert(k,arr[k])

    for i in range(0,n,1):
        print(int(list1[i]),end=' ')
    print()
