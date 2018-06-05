n = int(input())

cost = [int(x) for x in input().split()]
typ  = [int(y) for y in input().split()]

count1=0
count2=0
count3=0
cost1 = []
cost2 = []
cost3 = []

for i in range(0,n,1):
    if typ[i]==1:
        cost1.append(cost[i])
        count1+=1
    elif typ[i]==2:
        cost2.append(cost[i])
        count2+=1
    else:
        cost3.append(cost[i])
        count3+=1

if count1>0 and count2>0 and count3>0:
    min1 = min(cost1)
    min2 = min(cost2)
    min3 = min(cost3)
    if min1+min2 < min3:
        print(min1+min2)
    else:
        print(min3)

elif (count1==0 and count2!=0 and count3!=0) or (count1!=0 and count2==0 and count3!=0):
    print(min(cost3))
    
elif (count1!=0 and count2!=0 and count3==0):
    print(min(cost1)+min(cost2))

