# Write a Python program to swap first and last element of the list.

lst = [int(li) for li in input().split()]
lst[0],lst[-1] = lst[-1],lst[0]
print(lst)

# **** OUTPUT ****

# 1 2 3 4 5 
# [5, 2, 3, 4, 1]
