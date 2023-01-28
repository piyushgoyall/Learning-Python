# You have been given an array/list(ARR) of size N. You need to swap every pair of alternate elements in the array/list.
# You don't need to print or return anything, just change in the input array itself.
# Input Format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

# First line of each test case or query contains an integer 'N' representing the size of the array/list.

# Second line contains 'N' single space separated integers representing the elements in the array/list.
# Output Format :
# For each test case, print the elements of the resulting array in a single row separated by a single space.

# Output for every test case will be printed in a separate line.
# Sample Input 1:
# 1
# 6
# 9 3 6 12 4 32
# Sample Output 1 :
# 3 9 12 6 32 4
# Sample Input 2:
# 2
# 9
# 9 3 6 12 4 32 5 11 19
# 4
# 1 2 3 4
# Sample Output 2 :
# 3 9 12 6 32 4 11 5 19 
# 2 1 4 3 

**** SOLUTION ****

from sys import stdin

def swapAlternate(arr, n) :
    #Your code goes here
    a = 0
    b = 1
    for i in range(len(arr)//2):
        arr[a],arr[b] = arr[b],arr[a]
        a = a+2
        b = b+2
    return arr


#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#Printing the array/list
def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    arr, n = takeInput()
    if n != 0 :
        swapAlternate(arr, n)
        printList(arr, n)
    t -= 1
