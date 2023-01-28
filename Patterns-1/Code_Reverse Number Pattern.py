# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# 1
# 21
# 321
# 4321

## Read input as specified in the question
## Print the required output in given format

n=int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        print(i+1-j, end = '')
        j=j+1
    print()
    i=i+1
