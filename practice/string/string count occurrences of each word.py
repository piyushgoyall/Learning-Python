#2 Write a Python program to count the occurrences of each word in a given sentence.

sentence = input()
s1 = ""
for i in sentence:
    if i not in s1:
        s1 += i

for i in s1:
    count = 0
    for j in sentence:
        if i == j:
            count += 1
    print(i,count)
    
#     **** OUTPUT ****
    
# abcdeffedcba
# a 2
# b 2
# c 2
# d 2
# e 2
# f 2
