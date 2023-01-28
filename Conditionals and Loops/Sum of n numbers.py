# Given an integer n, find and print the sum of numbers from 1 to n.

# Read input as sepcified in the question
# Print output as specified in the question

n = int(input())
i = 0
while n>0:
    i = i + n
    n=n-1
print(i)

**** OR *****

n = int(input())
i = 1
sum = 0
while i<=n:
    sum += i
    i = i+1
print(sum)
