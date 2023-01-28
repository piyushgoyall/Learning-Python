#6 Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
# If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, 
# leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

add = input().strip()
add1 = ""
if len(add) > 2:
    if add[-3:] == "ing":
        add1 = add1 + add + "ly"
    else:
        add1 = add1 + add + "ing"
else:
    print(add)
print(add1)

# **** OUTPUT ****

# abc
# abcing
