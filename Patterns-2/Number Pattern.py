# Print the following pattern for n number of rows.
# Note: each line consist of equal number of characters + spaces. Suppose you are printing xth line for N=n. 
# You need to print 1..x followed by (n-x) spaces, again (n-x) spaces followed by x..1 For eg. N = 5 
#  1        1
#  12      21
#  123    321
#  1234  4321
#  1234554321


n = int(input())
ts = n*2 - 2
i = 1
while i <=n:
    j = 1
    while j <= i:
        print(j,end="")
        j = j+1
    spaces = 1
    while spaces <= ts:
        print(' ',end="")
        spaces = spaces+1
    ts = ts-2
    j = i
    while j > 0:
        print(j,end="")
        j = j-1
    i = i+1
    print()
