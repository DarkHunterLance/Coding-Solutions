n = int(input())

arr = [int(x) for x in input().split()]
res=0
for i in range(0,n,1):
    res = res + arr[i]

print(res)
