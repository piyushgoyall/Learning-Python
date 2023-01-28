# For n = 7 print the following output.

#       1 
#      2 2 
#     3 3 3 
#    4 4 4 4 
#   5 5 5 5 5 
#  6 6 6 6 6 6 
# 7 7 7 7 7 7 7

n = int(input())
for i in range(1,n+1):
    for spaces in range(n-i+1):
        print(" ",end="")
    for j in range(i):
        print(i,end=" ")
    print()
