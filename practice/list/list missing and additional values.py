# Write a Python program to find missing and additional values in two lists.
# Sample data : Missing values in second list: b,a,c
# Additional values in second list: g,h

li1 = [x for x in input().split()]
li2 = [y for y in input().split()]
li3 = []
for d in li1:
    for e in li2:
        if d == e:
            li2.remove(e)
            li3.append(e)
for f in li3:
    if f in li1:
        li1.remove(f)

print("Missing values in second list : ",li1)
print("Additional values in second list : ",li2)
print("Missing values in first list : ",li2)
print("Additional values in first list : ",li1)

# ***** OUTPUT ****

# 1 2 3 4 5 6 7 8
# 5 6 7 8 9 0
# Missing values in second list :  ['1', '2', '3', '4']
# Additional values in second list :  ['9', '0']
# Missing values in first list :  ['9', '0']
# Additional values in first list :  ['1', '2', '3', '4']
