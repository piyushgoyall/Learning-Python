# Write a program that rotates the element of a list so that the element at the
# first index moves to the second index, the element in the second index moves to
# the third index, etc., and the element in the last index moves to the first index.

a = [int(y) for y in input().split()]
b = a.pop(len(a)-1)
c = []
c.append(b)
print(c+a)

# **** OUTPUT ****

# 1 23 3 54 5 67 6 5 45 546 454 
# [454, 1, 23, 3, 54, 5, 67, 6, 5, 45, 546]
