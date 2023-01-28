#13 Write a Python program to find the first repeated character in a given string.

rep = input()
for i in range(len(rep)):
    flag = False
    for j in range(i+1,len(rep)):
        if rep[i] == rep[j]:
            flag = True
            print(rep[i])
            break
    if flag:
        break
        
# **** OUTPUT *****

# qwertyuiopoi
# i
