# Given a string, determine if it is a palindrome, considering only alphanumeric characters.
# Palindrome := A palindrome is a word, number, phrase, or other sequences of characters which read the same backwards and forwards.
# Example: If the input string happens to be, "malayalam" then as we see that this word can be read the same as forward and backwards, it is said to be a valid palindrome.
# The expected output for this example will print, 'true'.
# From that being said, you are required to return a boolean value from the function that has been asked to implement.
# Input Format: The first and only line of input contains a string without any leading and trailing spaces. All the characters in the string would be in lower case.
# Output Format: The only line of output prints either 'true' or 'false'.
# Note: You are not required to print anything. It has already been taken care of.
# Sample Input 1 : abcdcba
# Sample Output 1 : true 
# Sample Input 2: coding
# Sample Output 2: false

**** SOLUTION ****

from sys import stdin

def isPalindrome(string) :
	# Your code goes here
    if string == string[::-1]:
        return True
    else:
        return False

#main
string = stdin.readline().strip();
ans = isPalindrome(string)

if ans :
    print('true')
else :
    print('false')
