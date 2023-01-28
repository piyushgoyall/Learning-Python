#8 Write a Python program to swap comma and dot in a string. 
# Sample string: "32.054,23"
# Expected Output: "32,054.23"


# Python code to replace, with . and vice-versa

def Replace(str1):
    maketrans = str1.maketrans
    final = str1.translate(maketrans(',.', '.,', ' '))
    return final.replace(',', ", ")
 
string = "14, 625, 498.002"
print(Replace(string))

# swap = input()
# li = swap.split()
# print(li)
# for i in li:
#     for j in i:
#         if j == ". ":
#             li[i],li[j] = li[j],li[i]
# print(li)

# for i in range(len(swap)):
#     if swap[i] == "." or swap[i] == ",":
#         li.append(i)
# print(swap[:li[0]] + "." + swap[:li[1]] + "," + swap[li[1]+1:])

# **** OUTPUT ****

# 14.625.498, 002
