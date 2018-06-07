import random
tc = int(input())

for count in range(0,tc,1):
    k = int(input())

    n = random.randint(1,11)

    res = n*2 + k
    res = res/2
    res = res - n

    print(int(res))
