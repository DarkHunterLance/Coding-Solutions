tc = int(input())

for count in range(0,tc,1):
    flag=0
    s = input()

    list1 = list(s)

    for i in range(0,len(list1),1):
        if list1[i] == '2' and list1[i+1]=='1':
            flag+=1

    print(flag)
