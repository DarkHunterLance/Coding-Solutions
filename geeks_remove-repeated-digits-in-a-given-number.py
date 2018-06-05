tc = int(input())

for count in range(0,tc,1):
    n = input()

    x = list(n)

    s = sorted(set(x), key=x.index)

    res = ''.join(str(e) for e in s)

    print(res)
