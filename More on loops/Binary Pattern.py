# Print the following pattern for the given number of rows.
# Pattern for N = 4
#  1111
#  000
#  11
#  0

## Read input as specified in the question.
## Print output as specified in the question.

n = int(input())
p = n
for i in range(1,n+1,1):
    for j in range(1,p+1,1):
        if i%2 == 1:
            print(1,end="")
        else:
            print(0,end="")
    print()
    p = p-1
