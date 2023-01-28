#  Write a Program to determine if the given number is Armstrong number or not. Print true if number is armstrong, otherwise print false.
#  An Armstrong number is a number (with digits n) such that the sum of its digits raised to nth power is equal to the number itself.
#  For example,
#  371, as 3^3 + 7^3 + 1^3 = 371
#  1634, as 1^4 + 6^4 + 3^4 + 4^4 = 1634

#  Input Format : Integer n
#  Output Format : true or false

#  Sample Input 1 : 1
#  Sample Output 1 : true

#  Sample Input 2 : 103
#  Sample Output 2 : false

## Read input as specified in the question.
## Print output as specified in the question.

** SOLUTION **

def checkarmstr(num):
    sum = 0
    temp = num 
    order = len(str(num))
    while num > 0:
        rem = num%10
        sum = sum + rem**order
        num = num//10
        
    if temp == sum:
        return True
    else:
        return False
    

num = int(input())
isarmstrong = checkarmstr(num)
if(isarmstrong):
    print("true")
else:
    print("false")
