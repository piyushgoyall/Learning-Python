#2 Write a Python program to count the number of characters (character frequency) in a string.

s1 = input().strip()
s2 = ""
for i in s1:
    if i not in s2:
        s2 = s2+i
for i in s2:
    count = 0
    for j in s1:
        if i == j:
            count += 1
    print(i,count)
    
#     **** OUTPUT ****
    
# qwertyytrewqpi
# q 2
# w 2
# e 2
# r 2
# t 2
# y 2
# p 1
# i 1
