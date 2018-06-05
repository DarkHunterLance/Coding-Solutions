tc = int(input())

for count in range(0,tc,1):
    string = input()

    mylist = list(string)
    length = len(mylist)
    req = int(length/2)

    #print(req)

    if length%2==0:
        list1 = mylist[0:req:1]
        list2 = mylist[req::1]

    else:
        list1 = mylist[0:req:1]
        list2 = mylist[req+1::1]

    #print(list1,end = '+ ')
    #print(list2,end = ': ')
    #print()

    ch = 'a'
    flag=True
    for i in range(0,27,1):
        val=ord(ch)
        count1=0
        count2=0
        #print('CHECKING FOR '+ch)
        count1 = list1.count(ch)
        count2 = list2.count(ch)
        #print(count1,end = ', ')
        #print(count2)
        if count1==count2:
            ch = chr(val+1)
            continue
        else:
            print("NO")
            flag = False
            break

    if flag==True:
        print("YES")
