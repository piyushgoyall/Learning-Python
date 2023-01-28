# Find and display the largest number of a list without using built-in function


# max(). Your program should ask the user to input values in list from keyboard.

arr= [int(x) for x in input().split()]
maxim = -2**31
for i in range(len(arr)):
    if arr[i] > maxim:
        maxim = arr[i]
print(maxim)

# **** OUTPUT ****

# 12 23 43245 4523 23423 1324
# 43245
