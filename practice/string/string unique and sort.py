#4 Write a Python program that accepts a comma separated sequence of words as input and prints the 
# unique words in sorted form (alphanumerically). 
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white,red

sequence = input().split(",")
se1 = []
for i in sequence:
    if i not in se1:
        se1.append(i)
se1.sort()
for i in se1:
    print(i,end=",")    
    
# **** OUTPUT ****

# red, white, black, red, green, black
#  black, green, red, white,red,
