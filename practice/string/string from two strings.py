#5 Write a Python program to get a single string from two given strings, separated by a space and 
# swap the first two characters of each string. 
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

st1 = input().strip()
st2 = input().strip()
n1 = ""
n2 = ""
n1 = n1 + st2[0:2] + st1[2:]
n2 = n2 + st1[0:2] + st2[2:]
print(n1+" "+n2)
# print(n1)
# print(n2)
# for i in st1:

# **** OUTPUT ****

# abc
# xyz
# xyc abz
