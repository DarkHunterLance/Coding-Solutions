n = int(input())
arr = [int(x) for x in input().split()]

pos=0
neg=0
zero=0

for i in arr:
    if(i>0):
        pos+=1
    elif(i<0):
        neg+=1
    else:
        zero+=1

print(float(pos)/float(n))
print(float(neg)/float(n))
print(float(zero)/float(n))
