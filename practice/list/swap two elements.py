# Python program to swap two elements in a list.

l = [int(y) for y in input().split()]
position_1 = int(input())
position_2 = int(input())
l[position_1],l[position_2] = l[position_2],l[position_1]
print(l)

# **** OUTPUT ****

# 1 2 3 4 5 6 7 8 9 0
# 2
# 7
# [1, 2, 8, 4, 5, 6, 7, 3, 9, 0]
