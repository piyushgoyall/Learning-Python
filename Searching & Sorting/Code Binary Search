# You have been given a sorted(in ascending order) integer array/list(ARR) of size N and an element X. 
# Write a function to search this element in the given input array/list using 'Binary Search'. 
# Return the index of the element in the input array/list. In case the element is not present in the array/list, then return -1.
# Input format : The first line contains an Integer 'N' which denotes the size of the array/list.
# Second line contains 'N' single space separated integers representing the elements in the array/list.
# Third line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow..
# All the 't' lines henceforth, will take the value of X to be searched for in the array/list.
# Output Format : For each test case, print the index at which X is present, -1 otherwise.
# Output for every test case will be printed in a separate line.
# Sample Input 1:
# 7
# 1 3 7 9 11 12 45
# 1
# 3
# Sample Output 1:
# 1
# Sample Input 2:
# 7 
# 1 2 3 4 5 6 7
# 2
# 9 
# 7 
# Sample Output 2:
# -1
# 6

**** SOLUTION ****

from sys import stdin

def binarySearch(arr, n, x) :
    #Your code goes here
    low = 0
    high = n-1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == x:
            return mid
        if arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())
    
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


#main
arr, n = takeInput()
t = int(stdin.readline().strip())

while t > 0 :
    x = int(input().strip())    
    print(binarySearch(arr, n, x))
    t -= 1
