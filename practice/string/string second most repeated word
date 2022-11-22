#16 Write a Python program to find the second most repeated word in a given string.

li1 = input().split()
dict = {}
for i in li1:
    dict[i] = dict.get(i,0) + 1
    # li[0] = li[0] + 1

li2 = []
for i in dict:
    if dict[i] not in li2:
        li2.append(dict[i])

li2.sort()
for i in dict:
    if dict[i] == li2[-2]:
        print(i)
        break
