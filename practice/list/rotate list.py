# You have been given a random integer array/list(ARR) of size N. 
# Write a function that rotates the given array/list by D elements(towards the left).
# Sample Input 1:
# 1
# 7
# 1 2 3 4 5 6 7
# 2
# Sample Output 1:
# 3 4 5 6 7 1 2


lis = input("Input : ").split()
print("Entered list : ",lis)
dd = int(input("D : "))
surplus = dd
arr = []
print()
for i in range(0,len(lis)):
    for j in range(0,dd):
        if i < dd:
            flag = lis.pop(i)
            for pp in range(0,1):
                arr.append(flag)
        dd = dd-1
print("Rotated list : ",lis+arr)

# **** OUTPUT ****

# Input : 1 2 3 4 5 6 7 8 9 0
# Entered list :  ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# D : 4

# Rotated list :  ['5', '6', '7', '8', '9', '0', '1', '2', '3', '4']


# ******** OR ********

listtt = [int(lii) for lii in input().split()]
d = int(input())
new = []
new_2 = []
print(listtt)
for i in range(len(listtt)):
    if i >= d:
        new.append(listtt[i])
    else:
        new_2.append(listtt[i])
print(new)
print(new_2)
print(new+new_2)

# **** OUTPUT ****

# 1 2 3 4 5 6 7 8 9 0
# 4
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# [5, 6, 7, 8, 9, 0, 1, 2, 3, 4]
