# For n = 5 print the following pattern.

# 1234554321
# 1234**4321
# 123****321
# 12******21
# 1********1

n = int(input())
p = n
for i in range(1,n+1):
    for j in range(1,n+1):
        if j  <= n-i+1:
            print(j,end="")
        else:
            print("*",end="")
    k = p 
    for j in range(n+1,(2*n)+1):
        if j-i > n-1:
            print(k,end="")
            k = k-1
        else:
            print("*",end="")
    print()
    p = p-1

******** OR ********

n = int(input())
p = n
i = 1
while i <= n:
    j = 1
    while j <= n:
        if j <= n-i+1:
            print(j,end="")
        else:
            print("*",end="")
        j = j+1
    k = p
    j = n+1
    while j <= 2*n:
        if j - i > n-1:
            print(k,end="")
            k = k-1
        else:
            print("*",end="")
        j = j+1
    print()
    p = p-1
    i = i+1
