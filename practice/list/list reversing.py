# Reversing a List in Python.

rev = [int(r) for r in input().split()]
temp = []
for i in rev:
    temp.insert(0,i)
print(temp)
    
#     **** OUTPUT ****
    
#     1 2 3 4 5 6 7 8 9 0
# [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
