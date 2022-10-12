# Print the following pattern for a given n.
# For eg. N = 6

#  123456
#   23456
#    3456
#     456
#      56
#       6
#      56
#     456
#    3456
#   23456
#  123456


## Read input as specified in the question.
## Print output as specified in the question.


n = int(input())
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if i > j:
            print(" ",end="")
        else:
            p = j
            print(p,end="")
            p = p+1
    print()

for i in range(n+1,2*n,1):
    for j in range(1,n+1,1):
        if i+j < 2*n:
            print(" ",end="")
        else:
            q = j
            print(q,end="")
            q = q+1
    print()
