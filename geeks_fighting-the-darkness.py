def check(num,n):               #Function to check if the entire list consists of zeros
    countval = 0
    for i in range(0,n,1):
        if num[i]==0:
            countval += 1
            
    if countval==n:
        return False
    else:
        return True

tc = int(input())               # Taking the number of test cases as input

for count in range(0,tc,1):     # Iterating through the number of test cases
    n = int(input())            # Taking the size of each test case as input
    num = [int(x) for x in input().split()]         # Splitting the input into individual elements
    #print(num)

    #count = 0                   # Counter variable to keep track
    
    '''while check(num,n)==True:
        count+=1
        for i in range(0,n,1):
            if num[i]>0:
                 num[i] = num[i] - 1
            elif num[i]==0:
                 continue
        if all([v==0 for v in num])==True:
            break
        else:
            continue'''


    print(max(num))
