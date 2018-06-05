tc = int(input())

def rev(arr,n):
    for i in range(0,int(n/2),1):
        temp = arr[i]
        arr[i] = arr[n-1-i]
        arr[n-1-i] = temp
    return arr

for count in range(0,tc,1):
    n = int(input())

    finger = [int(x) for x in input().split()]
    glove = [int(y) for y in input().split()]
    tmp = glove

    #gloverev = rev(tmp,n)

    flagfront = True
    flagback = True

    for i in range(0,n,1):
        if finger[i]>glove[i]:
            flagfront = False

        if finger[i]>glove[n-1-i]:
           flagback = False

    #print(finger)
    #print(glove)

    if flagfront==True and flagback==False:
        print("front")
    elif flagfront==False and flagback==True:
        print("back")
    elif flagfront==True and flagback==True:
        print("both")
    elif flagfront==False and flagback==False:
        print("none")
