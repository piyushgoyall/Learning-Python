# You have been given a random integer array/list(ARR) of size N. You are required to find and return the second largest element present in the array/list.
# If N <= 1 or all the elements are same in the array/list then return -2147483648 or -2 ^ 31(It is the smallest value for the range of Integer)
# Input format : The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.
# The first line of each test case or query contains an integer 'N' representing the size of the array/list.
# The second line contains 'N' single space separated integers representing the elements in the array/list.
# Output Format : For each test case, print the second largest in the array/list if exists, -2147483648 otherwise.
# Output for every test case will be printed in a separate line.
# Sample Input 1:
# 1
# 7
# 2 13 4 1 3 6 28
# Sample Output 1:
# 13
# Sample Input 2:
# 1
# 5
# 9 3 6 2 9
# Sample Output 2:
# 6
# Sample Input 3:
# 2
# 2
# 6 6
# 4
# 90 8 90 5
# Sample Output 3:
# -2147483648
# 8

**** SOLUTION ****

# Take Minimum value as MIN_VALUE = -2147483648
from sys import stdin


def secondLargestElement(arr, n):
    #Your code goes here
    a = -2147483648
    b = -2147483648
    for i in range(n):
        if arr[i] > a:
            b = a
            a = arr[i]
        elif arr[i] > b and arr[i] != a:
            b = arr[i]
    return b


#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n
    return list(), 0

#main
t = int(stdin.readline().rstrip())
while t > 0 : 
    arr, n = takeInput()
    print(secondLargestElement(arr, n))
    t -= 1
