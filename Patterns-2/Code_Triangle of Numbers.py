# Print the following pattern for the given number of rows.
# Pattern for N = 4
#     1
#    232
#   34543
#  4567654

## Read input as specified in the question.
## Print output as specified in the question.

n = int(input())
i = 1
while i <= n:
    spaces = 1
    while spaces <= n-i:
        print(' ',end = "")
        spaces = spaces + 1
    p = i
    j = 1
    while j <= i:
        print(p,end = "")
        j = j+1
        p = p+1
    j = 1
    p = 2*i -2
    while j <= i-1:
        print(p,end = "")
        p = p-1
        j = j+1
    print()
    i = i+1
