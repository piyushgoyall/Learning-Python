# Find sum and average of List in Python

s = [int(u) for u in input().split()]
sum = 0
for m in s:
    sum = sum + m
print(sum)
avg = sum/len(s)
print(avg)

# **** OUTPUT ****

# 1 2 3 4 5 6 7 8 9 
# 45
# 5.0
