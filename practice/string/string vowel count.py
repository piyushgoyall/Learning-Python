#1 Write a program that accepts a string from user. Your program should count and display number of vowels in that string.

sti = input()
vowel = ["a","e","i","o","u","A","E","I","O","U"]
count = 0
for i in sti:
    if i in vowel:
        count = count+1
        print(i,end=" ")
print()
print(count)

# **** OUTPUT ****

# AEIOUHVC
# A E I O U 
# 5
