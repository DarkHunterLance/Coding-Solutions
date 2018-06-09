tc = int(input())

for count in range(0,tc,1):
    s = input()

    list1 = list(s)
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    list2 = [x for x in list1 if x in vowels]

    len2 = len(list2)
    k=0

    list3 = []

    for i in range(0,len(list1),1):
        if list1[i] not in vowels:
            list3.append(list1[i])
        else:
            list3.append(list2[len2-1-k])
            k = k+1

    print(''.join(str(e) for e in list3))
