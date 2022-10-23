# Aadil has been provided with a sentence in the form of a string as a function parameter. 
# The task is to implement a function so as to print the sentence such that each word in the sentence is reversed.
# Example: Input Sentence: "Hello, I am Aadil!"
# The expected output will print, ",olleH I ma !lidaA".
# Input Format: The first and only line of input contains a string without any leading and trailing spaces. The input string represents the sentence given to Aadil.
# Output Format: The only line of output prints the sentence(string) such that each word in the sentence is reversed. 
# Sample Input 1:
# Welcome to Coding Ninjas
# Sample Output 1:
# emocleW ot gnidoC sajniN
# Sample Input 2:
# Always indent your code
# Sample Output 2:
# syawlA tnedni ruoy edoc

**** SOLUTION ****

from sys import stdin

def reverseEachWord(string) :
	# Your code goes here
    arr = string.split(" ")
    li = ""
    for i in range(len(arr)):
        temp = arr[i]
        temp = temp[::-1]
        li = li + temp + " "
        
    return li

#main
string = stdin.readline().strip()

ans = reverseEachWord(string)

print(ans)

**** OR ****

from sys import stdin 

def reverseWord(string, start, end) : 
    reverse = "" 
    while start < end : 
        reverse = string[start] + reverse 
        start += 1 
    return reverse 
        
def reverseEachWord(string) : 
    n = len(string) 
    previousSpaceIndex = -1 
    ans = "" 
    i = 0
    while i < n : 
        if string[i] == ' ' : 
            ans += (reverseWord(string, previousSpaceIndex + 1, i) + " ") 
            previousSpaceIndex = i 
        i += 1 
    ans += (reverseWord(string, previousSpaceIndex + 1, i) + " ") 
    return ans 

#main 
string = stdin.readline().strip() 
ans = reverseEachWord(string) 
print(ans)
