arr1 = [int(x) for x in input().split()]
arr2 = [int(y) for y in input().split()]

alice = 0
bob = 0

for i in range(0,3,1):
    if(arr1[i] > arr2[i]):
        alice+=1
    elif(arr1[i] < arr2[i]):
        bob+=1
    else:
        continue

print(str(alice) + ' ' + str(bob))
