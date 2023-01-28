# Write a program to generate the reverse of a given number N. Print the corresponding reverse number.
# Note : If a number has trailing zeros, then its reverse will not include them. For e.g., reverse of 10400 will be 401 instead of 00401.
# Input format :
# Integer N
# Output format :
# Corresponding reverse number
# Sample Input 1 :
# 1234
# Sample Output 1 :
# 4321

#Write Your Code Here

n=int(input())
rev=0
while n!=0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)
