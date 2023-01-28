# Print the following pattern for the given number of rows.
# Note: N is always odd.
# Pattern for N = 5
#    *  
#   *** 
#  *****
#   *** 
#    * 

## Read input as specified in the question.
## Print output as specified in the question.


n = int(input())
p = (n//2)+1
for i in range(1,p+1,1):
    for j in range(1,n+1,1):
        if i+j <= p or j-i >= p:
            print(" ",end="")
        else:
            print("*",end="")
    print()
    
for i in range(p+1,n+1,1):
    for j in range(1,n+1,1):
        if i-j >= p or i+j > n+p:
            print(" ",end="")
        else:
            print("*",end="")
    print()
