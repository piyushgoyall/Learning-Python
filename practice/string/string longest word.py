#8 Write a Python function that takes a list of words and return the longest word and the length of the longest one.
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9

longest = input().strip()
l1 = longest.split(" ")
h = 0
for i in l1:
    if len(i) > h:
        h = len(i)
        maximum = i
print("Length of the longest word : ",h)
print("Longest word : ",maximum)
#     for j in i:
#         h = len(j)
# print(h)

# **** OUTPUT ****

# Python program to get a string 
# Length of the longest word :  7
# Longest word :  program
