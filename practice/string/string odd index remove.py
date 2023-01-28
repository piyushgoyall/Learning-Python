#1 Write a Python program to remove the characters which have odd index values of a given string.

string = input()
st1 = ""
for i in range(0,len(string),2):
    st1 += string[i]
print(st1)

# **** OUTPUT ****

# abcdefgh12345678
# aceg1357
