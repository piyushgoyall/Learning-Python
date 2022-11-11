# For n = 5 print the following patttern.

# 1 2 3 4 5 
#  2 3 4 5 
#   3 4 5 
#    4 5 
#     5 
#    4 5 
#   3 4 5 
#  2 3 4 5 
# 1 2 3 4 5 

n = int(input())
for i in range(n):
    for spaces in range(i):
        print(" ",end="")
    for j in range(i+1,n+1):
        print(j,end=" ")
    print()
for i in range(n-1):
    for spaces in range(n-2,i,-1):
        print(" ",end="")
    for j in range(n-i-1,n+1):
        print(j,end=" ")
    print()
