# You have been given a random integer array/list(ARR) of size N. Write a function that rotates the given array/list by D elements(towards the left).
# Note: Change in the input array/list itself. You don't need to return or print the elements.
# Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.
# First line of each test case or query contains an integer 'N' representing the size of the array/list.
# Second line contains 'N' single space separated integers representing the elements in the array/list.
# Third line contains the value of 'D' by which the array/list needs to be rotated.
# Output Format :
# For each test case, print the rotated array/list in a row separated by a single space.
# Output for every test case will be printed in a separate line.
# Sample Input 1:
# 1
# 7
# 1 2 3 4 5 6 7
# 2
# Sample Output 1:
# 3 4 5 6 7 1 2
# Sample Input 2:
# 2
# 7
# 1 2 3 4 5 6 7
# 0
# 4
# 1 2 3 4
# 2
# Sample Output 2:
# 1 2 3 4 5 6 7
# 3 4 1 2

**** SOLUTION ****

from sys import stdin

def swap(arr,start,end):
    arr[start],arr[end] = arr[end],arr[start]
    
def rev(arr,start,end):
    while start < end:
        swap(arr,start,end)
        start = start+1
        end = end-1
        

def rotate(arr, n, d):
    if n == 0:
        return
    if d >= n and n != 0:
        d = d%n
    rev(arr,0,n-1)
    rev(arr,0,n-d-1)
    rev(arr,n-d,n-1)


#Taking Input Using Fats I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n

#to print the array/list 
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()

#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    arr, n = takeInput()
    d = int(stdin.readline().rstrip())
    rotate(arr, n, d)
    printList(arr, n)
    
    t -= 1
