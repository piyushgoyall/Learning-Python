#4 Write a Python program to get a string from a given string where 
# all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

change = input().strip()
# new = change[0]
# n1 = ''+new
# for i in range(1,len(change)):
#     if change[i] == new:
#         n1 = n1 + "$"
#     else:
#         n1 = n1 + change[i]


# new = ""
# for i in range(0,len(change)):
#     for j in range(i+1,len(change)):
#         if change[i] == change[j]:
            
#             new = change[:j-1]+"&"+change[j:]

#             print(j)
#         else:
#             new = new + change[i]
            
# print(new)


new = ""
for i in range(0,1):
    new+=change[i]
    for j in range(i+1,len(change)):
        if change[i] == change[j]:
            new += "&"
        else:
            new+=change[j]
print(new)

# **** OUTPUT ****

# restartert
# resta&te&t
