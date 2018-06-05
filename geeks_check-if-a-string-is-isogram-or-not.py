tc = int(input())

for count in range(0,tc,1):
    flag = True
    s = input()

    list1 = list(s)
    list2 = []

    for i in range(97,123,1):
        c = list1.count(chr(i))
        list2.append(c)

    for i in range(0,26,1):
        if list2[i]>1:
            flag= False
            break
        else:
            continue

    if flag==True:
        print('1')
    else:
        print('0')
