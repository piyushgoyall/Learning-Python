# 5. Write a program that input a string and ask user to delete a given word from a string.

string = input()
x = input()
temp = string.split(" ")
for i in temp:
    if i!=x:
        print(i,end=" ")
        
# **** OUTPUT ****

# one two three four five
# three
# one two four five 
