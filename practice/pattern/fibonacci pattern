For n = 5 print the following pattern.

# 1 
# 1 2
# 3 5 8
# 13 21 34 55
# 89 144 233 377 610


n = int(input())
a = 0
b = 1
sum = 0
for i in range(0,n+1):
    for j in range(i):
        sum = a+b
        a = b
        b = sum
        print(a,end="  ")
    print()
