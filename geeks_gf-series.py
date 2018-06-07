import time
tc = int(input())

def series(a,b):
    return ((a*a)-b)


for count in range(0,tc,1):
    n = int(input())
    #print('WITH FUNCTION CALL')
    t = time.time()

    a = 0
    b = 1

    if n==0:
        continue
    elif n==1:
        print('0')
        continue

    print(str(a)+' '+str(b),end=' ')

    for i in range(2,n,1):
        res = series(a,b)
        print(res,end=' ')
        a = b
        b = res
    print()
    #print('Time required : '+str(time.time()-t)+' secs')
    #print()

    #-------------------------------------------------------#

    '''print('WITHOUT FUNCTION CALL')
    t = time.time()
    a = 0
    b = 1

    print(str(a)+' '+str(b),end=' ')

    for i in range(2,n,1):
        res = (a*a)-b
        print(res,end=' ')
        a = b
        b = res
    print()
    print('Time required : '+str(time.time()-t)+' secs')'''

   
