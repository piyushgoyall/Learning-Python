#5 Write a Python program to check whether a string contains all letters of the alphabet.

alphabet = input()
alpha = "abcdefghijklmonpqrstuvwxyz" 
# ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in alpha:
    if i not in alphabet.lower():
        print("String does not contain all letters of the alphabet.")
        break
    else:
        print("String contains all letters of the alphabet.")
        break
        
# **** OUTPUT ****

# qwertyuioplkjhgfdsazxcvbnm
# String contains all letters of the alphabet.

# ** AND **

# qwertyuiop
# String does not contain all letters of the alphabet.
