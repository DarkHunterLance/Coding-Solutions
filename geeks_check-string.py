tc = int(input())

for count in range(0,tc,1):
    s = input()

    list1 = list(s)

    temp = [list1[0]*len(list1)]

    res = ''.join(str(e) for e in temp)

    if res==s:
        print("YES")
    else:
        print("NO")
