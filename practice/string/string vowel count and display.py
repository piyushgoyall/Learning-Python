#9 Write a Python program to count and display the vowels of a given text.

vowel = input()
v = "aeiouAEIOU"
count = 0
for i in vowel:
    if i in v:
        count += 1
        print(i,end=" ")
print()
print("Count of vowels : ",count)

# **** OUTPUT ****

# ioweutvpnocxtmo
# i o e u o o 
# Count of vowels :  6
