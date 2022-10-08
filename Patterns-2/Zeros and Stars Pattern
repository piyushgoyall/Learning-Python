# Print the following pattern
# Pattern for N = 4
# *000*000*
# 0*00*00*0
# 00*0*0*00
# 000***000

## Read input as specified in the question.
## Print output as specified in the question.

n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= 2*n + 1:
        if i == j or j == n+1 or j+i == (n+1)*2:
            print("*",end="")
        else:
            print("0",end="")
        j = j+1
    print()
    i = i+1
