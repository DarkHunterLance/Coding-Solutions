n = 10000
maximum = 0

for i in range(1,n,1):
    temp = i
    count=1

    while(temp!=1):
        if(temp%2==0):
            temp=temp/2
        else:
            temp=(3*temp)+1
        count+=1

    if(count>maximum):
        maximum=count
        pos= i

print(str(pos)+' : '+str(maximum))

n = pos
while(pos!=1):
        if(pos%2==0):
            pos=pos/2
        else:
            pos=(3*pos)+1
        count+=1
        print(int(pos),end=',')
