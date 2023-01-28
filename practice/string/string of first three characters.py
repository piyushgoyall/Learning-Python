#8 Write a Python function to get a string made of its first three characters of a specified string. 
# If the length of the string is less than 3 then return the original string. 
# Sample function and result :
# first_three('ipy') -> ipy
# first_three('python') -> pyt

three = input().strip()
if len(three) < 3:
    print(three)
else:
    print(three[0:3])
    
# **** OUTPUT ****

# python
# pyt
