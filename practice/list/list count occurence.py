# Count occurrences of an element in a list in Python.

c = [int(o) for o in input().split()]
count = 0
x = int(input())
for search in c:
    if search == x:
        count = count+1
print(count)

# **** OUTPUT ****

# 1 2 3 4 5 6 7 8 9 9 8 4 5 6 3 4
# 4
# 3
