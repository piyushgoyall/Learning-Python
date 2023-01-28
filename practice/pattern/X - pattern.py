For n = 4 print the following pattern.

# 1     1
#  2   2
#   3 3
#    4
#   3 3
#  2   2
# 1     1

n = int(input())
k = n-1
for i in range(1,n+1):
    for j in range(1,2*n):
        if i == j or i+j == 2*n:
            print(i,end="")
        else:
            print(" ",end="")
    print()
for i in range(1,n):
    for j in range(1,2*n):
        if i+j == n or j-i == n:
            print(k,end="")
        else:
            print(" ",end="")
    print()
    k = k-1
