#4 Write a Python program to print the index of the character in a string. 
# Sample string: w3resource
# Expected output:
# Current character w position at 0
# Current character 3 position at 1
# Current character r position at 2
# - - - - - - - - - - - - - - - - - - - - - - - - -
# Current character c position at 8
# Current character e position at 9

index = input()
for i in range(len(index)):
    print(f"Current character {index[i]} position at {i}")
    
# **** OUTPUT ****

# qwerty
# Current character q position at 0
# Current character w position at 1
# Current character e position at 2
# Current character r position at 3
# Current character t position at 4
# Current character y position at 5
