# Print the following pattern for n = 5.

# 1 2 3 4 5
# 2 2 3 4 5
# 3 3 3 4 5
# 4 4 4 4 5
# 5 5 5 5 5

n = int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i >= j:
            print(i,end="")
        else:
            print(j,end="")
    print()
