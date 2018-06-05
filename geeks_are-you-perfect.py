import math

tc = int(input())

for count in range(0,tc,1):
    n = int(input())
    res = math.sqrt(n)
    flag = True
    temp1 = n
    temp2 = n

    if (res-int(res))==0:
        print(str(n)+' '+'0')
        continue
    else:
        while flag==True:
            temp1 = temp1+1
            temp2 = temp2-1
            res1 = math.sqrt(temp1)
            res2 = math.sqrt(temp2)
            
            if (res1-int(res1))==0:
                flag = False
                pos = temp1
                break

            if (res2-int(res2))==0:
                flag = False
                pos = temp2
                break
    if pos>n:
         print(str(pos)+' '+str(pos-n))
    elif pos<n:
         print(str(pos)+' '+str(n-pos))   
