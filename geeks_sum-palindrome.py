tc = int(input())

def rev(n):
    list1 = list(str(n))
    list2 = []

    for i in range(0,len(list1),1):
        list2.append(list1[len(list1)-1-i])

    return int(''.join(str(e) for e in list2))

for count in range(0,tc,1):
    n = int(input())
    initial = n
    flag = 0

    reverse = rev(n)

    #print("Initial : ",initial)
    #print("Reverse : ",reverse)

    if n==reverse:
        print(n)
        continue
    else:
        while n!=reverse and flag<5:
            print("After iteration "+str(flag)+" : n = "+str(n))
            flag = flag+1
            n = n+reverse
            reverse = rev(n)
            print("Initial :"+str(initial)+"\t n :"+str(n)+"\t reverse :"+str(reverse))
            

        if n==reverse:
            print(n)
            continue
        else:
            print(-1)
            continue
