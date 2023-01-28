# Python program to check if a number is armstrong or not.

n = int(input())
temp = n
sum = 0
while n > 0:
    rem = n%10
    sum = sum + rem**3
    n = n//10
    
if sum==temp:
    print("Armstrong number")
else: 
    print("Not an armstrong number")
