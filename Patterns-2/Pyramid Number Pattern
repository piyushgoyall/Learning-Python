# Print the following pattern for the given number of rows.
# Pattern for N = 4
#    1
#   212
#  32123
# 4321234

## Read input as specified in the question.
## Print output as specified in the question.

n = int(input())
i = 1
while i <= n:
    spaces = 1
    while spaces <= n-i:
        print(' ',end="")
        spaces = spaces+1
        
    j = 1
    p = i
    while j <= i:
        print(p,end="")
        j = j+1
        p = p-1
    
    p = 2
    while p <= i:
        print(p,end="")
        p = p+1
    i = i+1
    print()
