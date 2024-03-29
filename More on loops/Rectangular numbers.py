# Print the following pattern for the given number of rows.
# Pattern for N = 4


#   4 4 4 4 4 4 4
#   4 3 3 3 3 3 4
#   4 3 2 2 2 3 4
#   4 3 2 1 2 3 4
#   4 3 2 2 2 3 4
#   4 3 3 3 3 3 4  
#   4 4 4 4 4 4 4


## Read input as specified in the question.
## Print output as specified in the question.


n = int(input())
for r in range(1,2*n,1):
    i = n
    if r <= n:
        for c in range(1,2*n,1):
            print(i,end="")
            if r > c:
                i = i-1
            if r+c >= 2*n:
                i = i+1
    if r > n:
        for c in range(1,2*n,1):
            print(i,end="")
            if r+c < 2*n:
                i = i-1
            if r <= c:
                i = i+1
    print()
    
    
    # ******** OR ********
    
n = int(input())
k = n
for i in range(1,n):
    for j in range(1,n):
        if i <= j:
            print(n-i+1,end="")
        else:
            print(n-j+1,end="")
    for j in range(n+1,2*n+1):
        if (j-n)<k:
            print(k,end="")
        else:
            print(j-n,end="")
    k = k-1
    print()
spaces = n    
for i in range(1,n+1):
    temp = n
    for spaces in range(1,n-i+1):
        print(temp,end="")
        temp = temp-1
    for j in range(i-1):
        print(i,end="")
    for j in range(n+1,2*n+1):
        if i >= (j-n):
            print(i,end="")
        else:
            print(j-n,end="")
    print()
