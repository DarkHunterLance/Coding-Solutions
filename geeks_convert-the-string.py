tc = int(input())

for count in range(0,tc,1):
    s = input()

    list1 = list(s)
    list2 = []
    vowels = ['a','e','i','o','u','A','E','I','O','U']

    for i in range(0,len(list1),1):
        if list1[i] in vowels:
            continue
        elif list1[i] not in vowels:
            list2.append('#')
            if ord(list1[i])>=65 and ord(list1[i])<=90:
                temp = chr(ord(list1[i])+32)
                list2.append(temp)
            elif ord(list1[i])>=97 and ord(list1[i])<=122:
                temp = chr(ord(list1[i])-32)
                list2.append(temp)

    print(''.join(str(e) for e in list2))
