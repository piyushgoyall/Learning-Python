# 7. Write a program with a function that accepts a string from keyboard and
# create a new string after converting character of each word capitalized. For
# instance, if the sentence is "stop and smell the roses" the output should be "Stop And Smell The Roses"

str = ""
temp = input().split()
for i in range(len(temp)):
    for j in range(len(temp[i])):
        if j == 0:
            str = str + chr(ord(temp[i][0])-32)
        else:
            str = str + temp[i][j]
    str = str + " "
print(str)

# ** OUTPUT **

# stop and smell the roses
# Stop And Smell The Roses 
# ------------------------
# you just got rick rolled
# You Just Got Rick Rolled 


# **** OR ****


s = [x for x in input().split()]
new=''
for i in s:
    new += i[0].upper()
    new += i[1:]
    new += " "
print(new)

# ** OUTPUT **

# stop and smell the roses
# Stop And Smell The Roses 
# ------------------------
# you just got rick rolled
# You Just Got Rick Rolled 
