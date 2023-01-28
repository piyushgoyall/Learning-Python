# Write a program to input an integer N and print the sum of all its even digits and sum of all its odd digits separately.
# Digits mean numbers, not the places! That is, if the given integer is "13245", even digits are 2 & 4 and odd digits are 1, 3 & 5.
# Input format : Integer N
# Output format : Sum_of_Even_Digits Sum_of_Odd_Digits
# (Print first even sum and then odd sum separated by space)
# Sample Input 1:
# 1234
# Sample Output 1:
# 6 4
# Sample Input 2:
# 552245
# Sample Output 2:
# 8 15

## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
## print(val1, " ", val2)

n=int(input())
rev=0
even=0
odd=0
while n!=0:
    rem=n%10
    if rem%2==0:
        even=even+rem
    elif rem%2==1:
        odd=odd+rem
    n=n//10
print(even,odd) 
