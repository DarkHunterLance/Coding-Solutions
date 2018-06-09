tc = int(input())

for count in range(0,tc,1):
    s = input()

    list1 = list(s)

    for i in range(0,len(list1),1):
        print(list1[len(list1)-1-i],end='')

    print()
