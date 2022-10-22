# For a given string(str), remove all the consecutive duplicate characters.
# Example:
# Input String: "aaaa"
# Expected Output: "a"

# Input String: "aabbbcc"
# Expected Output: "abc"
# Input Format: The first and only line of input contains a string without any leading and trailing spaces. All the characters in the string would be in lower case.
# Output Format: The only line of output prints the updated string.
# Sample Input 1:
# aabccbaa
# Sample Output 1:
# abcba
# Sample Input 2:
# xxyyzxx
# Sample Output 2:
# xyzx

**** SOLUTION ****

from sys import stdin

def removeConsecutiveDuplicates(string) :
	# Your code goes here
    s = string + " "
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            print(s[i],end="")

#main
string = stdin.readline().strip()
removeConsecutiveDuplicates(string)


**** OR ****

from sys import stdin

def removeConsecutiveDuplicates(string) :
	# Your code goes here
	n = len(string)
  
	if n == 0:
	    return string
	
	answer = ""
	start = 0
	while start < n:
	    uniq = string[start]
	    nextuniq = start + 1
	    
	    while nextuniq < n and string[nextuniq] == uniq:
	        nextuniq = nextuniq + 1
	        
	    answer = answer + uniq
	    start = nextuniq
	return answer
  
#main
string = stdin.readline().strip()
ans = removeConsecutiveDuplicates(string)
print(ans)

