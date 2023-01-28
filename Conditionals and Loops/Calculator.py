# Write a program that performs the tasks of a simple calculator. 
# The program should first take an integer as input and then based on that integer perform the task as given below.
# 1. If the input is 1, then 2 integers are taken from the user and their sum is printed.
# 2. If the input is 2, then 2 integers are taken from the user and their difference(1st number - 2nd number) is printed.
# 3. If the input is 3, then 2 integers are taken from the user and their product is printed.
# 4. If the input is 4, then 2 integers are taken from the user and the quotient obtained (on dividing 1st number by 2nd number) is printed.
# 5. If the input is 5, then 2 integers are taken from the user and their remainder(1st number mod 2nd number) is printed.
# 6. If the input is 6, then the program exits.
# 7. For any other input, then print "Invalid Operation".
# Note: Each answer in next line.
# Input format:
# Take integers as input, in accordance to the description of the question. 
# Output format:
# The output lines must be as prescribed in the description of the question.
# Sample Input:
# 3
# 1
# 2
# 4
# 4
# 2
# 1
# 3
# 2
# 7
# 6
# Sample Output:
# 2
# 2
# 5
# Invalid Operation

# Explanation of the sample input
# The first number given is 3, so that means two more numbers will be given and we'll have to multiply them and show the result. 
# The two numbers are 1 and 2. Their product is 2, so 2 is displayed first in the output. Similarly, all the numbers are processed in groups of three. 
# The first number tells the operation and the next two numbers tell on which numbers the operation is done. This applies to numbers from 1 to 5. 
# If the input is 6 (like it is at the end), two more numbers will NOT be provided, you simply have to exit the program. 
# Also, if the input is any number except 1 to 6 (like 7 which is at the second last), then you simply have to print "Invalid Operation"

**** SOLUTION ***

# Write your code here
n=int(input())
while n!=6:
    if n<=5 and n>=1:
        a=int(input())
        b=int(input())
    if n==1:
        print(a+b)
    if n==2:
        print(a-b)
    if n==3:
        print(a*b)
    if n==4:
        print(a//b)
    if n==5:
        print(a%b)
    elif n<1 or n>6:
        print("Invalid Operation")
    n=int(input())
