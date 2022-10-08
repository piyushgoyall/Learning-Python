# Print the following pattern for the given number of rows.
# Note: N is always odd.

# Pattern for N = 5
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

n = int(input())
i = 1
while i <= (n+1)//2:
    spaces = 1
    while spaces <= ((n+1)//2-i):
        print(' ',end="")
        spaces = spaces+1
    j = 1
    while j <= (2*i)-1:
        print("*",end="")
        j = j+1
    print()
    i = i+1
    
i = n//2
while i >= 1:
    spaces = 1
    while spaces <= (n//2-i+1):
        print(" ",end="")
        spaces = spaces+1
    j = 1
    while j <= (2*i)-1:
        print("*",end="")
        j = j+1
    print()
    i = i-1
