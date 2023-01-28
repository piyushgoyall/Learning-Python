# Print the following pattern for the given number of rows.
# Assume N is always odd.
# Note : There is space after every star.
# Pattern for N = 7

#  * 
#   * * 
#    * * * 
#     * * * * 
#    * * * 
#   * * 
#  *

n = int(input())
i = 1
p = (n-1)/2
m = (n+1)/2
while i <= m:
    spaces = 2
    while spaces <= i:
        print(" ",end="")
        spaces = spaces+1 
    stars = 1
    while stars <= i:
        print("* ",end="")
        stars = stars + 1
    print()
    i = i+1

i = 1
a = 0
while i <= p:
    r = p - 1
    while r >= i:
        print(" ",end="")
        r = r-1
    
    r = p-1
    while r >= a:
        print("* ",end="")
        r = r-1
    print()
    i = i+1
    a = a+1
