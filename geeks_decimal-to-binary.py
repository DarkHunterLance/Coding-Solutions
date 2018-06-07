tc = int(input())

for count in range(0,tc,1):
    n = int(input())
    forward = []
    back = []

    while(n>0):
        r = int(n%2)
        forward.append(r)
        n = int(n/2)

    for i in range(0,len(forward),1):
        back.append(forward[len(forward)-1-i])

    res = ''.join(str(x) for x in back)
    print(res)
