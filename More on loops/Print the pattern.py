# Print the following pattern for the given number of rows.
# Pattern for N = 5
#   1    2   3    4   5
#   11   12  13   14  15
#   21   22  23   24  25
#   16   17  18   19  20
#   6    7    8   9   10

# Input format : N (Total no. of rows)
# Output format : Pattern in N lines

# Sample Input : 4
# Sample Output :
#   1  2  3  4
#   9 10 11 12
#  13 14 15 16
#   5  6  7  8

*Solution*

n = int(input())
p = n//2
c = 0
a = 0
b = 0
if n%2 == 1:
    for i in range(1,p+2,1):
        for j in range(1,n+1,1):
            print(j+c,end=" ")
        print()
        c = c+2*n
    a = c-n
    b = a-(2*n-1)
    d = b
    for i in range(p+2,n+1,1):
        for j in range(1,n+1,1):
            print(d,end=" ")
            d = d+1
        print()
        d = d-3*n
elif n%2 == 0:
    for i in range(1,p+1,1):
        for j in range(1,n+1,1):
            print(j+c,end=" ")
        print()
        c = c+2*n
    a = c
    b = a-n+1
    d = b
    for i in range(p+1,n+1,1):
        for j in range(1,n+1,1):
            print(d,end=" ")
            d = d+1
        print()
        d = d-3*n
