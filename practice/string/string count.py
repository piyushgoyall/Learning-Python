#2 Write a program that reads a string from keyboard and display:

#  * The number of uppercase letters in the string

#  * The number of lowercase letters in the string

#  * The number of digits in the string
 
#  * The number of whitespace characters in the string

read = input()
ucount = 0
lcount = 0
dcount = 0
wcount = 0
for i in read:
    if (i>=chr(65) and i<=chr(90)):
        ucount += 1
    elif (i>=chr(97) and  i<=chr(122)):
        lcount += 1
    elif (i>=chr(48) and i<=chr(57)):
        dcount += 1
    elif i == " ":
        wcount += 1
print("Total uppercase letters : ",ucount)
print("Total lowercase letters : ",lcount)
print("Total digits : ",dcount)
print("Total whitespces : ",wcount)

# **** OUTPUT ****

# QWERT     qwert     12345
# Total uppercase letters :  5
# Total lowercase letters :  5
# Total digits :  5
# Total whitespces :  10
