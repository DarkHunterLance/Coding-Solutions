tc = int(input())

def test(ch):
    if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
        return True
    elif ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
        return True
    return False

for count in range(0,tc,1):
    s = input()
    list1 = list(s)

    res = []

    for i in range(0,len(list1),1):
        x = test(list1[i])

        if x==True:
            continue
        else:
            res.append(list1[i])

    res = ''.join(str(e) for e in res)
    print(res)
