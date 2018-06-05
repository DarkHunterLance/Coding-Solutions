n = int(input())
star = '#'
space = ' '

for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if(j>= n+1-i):
            print(star,end = '')
        else:
            print(space,end = '')
    print()
