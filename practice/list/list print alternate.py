# Write a program that accepts a list from user and print the alternate element of list.

lis = input().split()
print(lis)
for i in range(0,len(lis),2):
    print(lis[i],end=' ')
    
# **** OUTPUT ****

# 1 2 3 4 4 3 2 1 2 
# ['1', '2', '3', '4', '4', '3', '2', '1', '2']
# 1 3 4 2 2 
