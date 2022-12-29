# Write a program to do basic string compression. For a character which is consecutively repeated more than once, 
# replace consecutive duplicate occurrences with the count of repetitions.
# Example:
# If a string has 'x' repeated 5 times, replace this "xxxxx" with "x5".
# The string is compressed only when the repeated character count is more than 1.
# Note:
# Consecutive count of every character in the input string is less than or equal to 9.
# Input Format:
# The first and only line of input contains a string without any leading and trailing spaces.
# Output Format:
# The output contains the string after compression printed in single line.
# Note:
# You are not required to print anything. It has already been taken care of. Just implement the given function.
# Sample Input 1:
# aaabbccdsa
# Sample Output 1:
# a3b2c2dsa
# Explanation for Sample Output 1:
# In the given string 'a' is repeated 3 times, 'b' is repeated 2 times, 'c' is repeated 2 times and 'd', 's' and 'a' and occuring 1 time 
# hence no compression for last 3 characters.
# Sample Input 2:
# aaabbcddeeeee
# Sample Output 2:
# a3b2cd2e5
# Explanation for Sample Output 2:
# In the given string 'a' is repeated 3 times, 'b' is repeated 2 times, 'c' is occuring single time, 'd' is repeating 2 times and 'e' is repeating 5times.

**** SOLUTION ****

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def getCompressedString(input) :
	# Write your code here.
	n = len(string)
	ans = ""
	count = 1
	ans = ans + string[0]
	for i in range(1,n):
	    if string[i] == string[i-1]:
	        count = count + 1
	    else:
	        if count > 1:
	            ans = ans + str(count)
	            count = 1
	        ans = ans + string[i]
	        
	if count > 1:
	    ans = ans + str(count)
	return ans

# Main.
string = stdin.readline().strip();
ans = getCompressedString(string)
print(ans)


**** OR ****

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def getCompressedString(n) :
	# Write your code here
	n=n+" "
	ans = ''+n[0]
	count = 1
	for i in range(1, len(n)):
		if n[i] == ans[-1]:
			count += 1
		else:
			if count > 1:
				ans += str(count)
			ans += n[i]
			count = 1
	return ans.strip()


# Main.
string = stdin.readline().strip();
ans = getCompressedString(string)
print(ans)

