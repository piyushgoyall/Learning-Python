#7 Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, 
# if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

sub = input().strip()
o = sub.index("not")
t = sub.index("poor")
print(sub[:o] + "good" + sub[t+4:])

# **** OUTPUT ****

# The lyrics is not that poor!
# The lyrics is good!
