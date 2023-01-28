# 1 Write a Python program to strip a set of characters from a string.

sets = input()
strip = input().split()
for i in sets:
    if i not in strip:
        print(i,end=" ")
#     for j in strip:
#         if i != j:
#             print(i)

# **** OUTPUT ****

# house mouse lounge
# o u e
# h s   m s   l n g 
