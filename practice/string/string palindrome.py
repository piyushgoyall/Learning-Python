#10 A palindrome is a string that reads the same backward as forward. For example, the words dad,
# madam and radar are all palindromes. Write a programs that determines whether the string is a
# palindrome.
# Note: do not use reverse() method.

n=input().strip()
rev=n[::-1]
if n==rev:
    print("Palindrome")
else:
    print("Not palindrome")
    
# **** OUTPUT ****

# hiy
# Not palindrome
