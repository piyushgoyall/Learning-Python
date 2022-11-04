# Print the following pattern for n = 7.

# *
# --
# ***
# ----
# *****
# ------
# *******
# ------
# *****
# ----
# ***
# --
# *

n = int(input())
k = n
for i in range(0,n+1):
    for j in range(i):
        if i%2==0:
            print("-",end="")
        else:
            print("*",end="")
    print()
for i in range(n+1,2*n):
    for j in range(k-1):
        if i%2==0:
            print("-",end="")
        else:
            print("*",end="")
    print()    
    k = k-1
