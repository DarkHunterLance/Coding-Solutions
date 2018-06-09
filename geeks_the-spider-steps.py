tc = int(input())

for count in range(0,tc,1):
    [H,U,D] = [int(x) for x in input().split()]

    base = 0
    flag = False
    steps = 0

    while base<H:
        #print(base,end =',')
        if base+U>=H:
            steps+=1
            base = base + U
        elif (base+U)<H:
            steps+=1
            base = base + (U-D)

    if base==H:
        print(steps+1)
    elif base>H:
        print(steps)
        
