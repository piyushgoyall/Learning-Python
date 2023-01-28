# You have been given a random integer array/list(ARR) and a number X. Find and return the number of triplets in the array/list which sum to X.
# Note : Given array/list can contain duplicate elements.
# Input format : The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.
# First line of each test case or query contains an integer 'N' representing the size of the first array/list.
# Second line contains 'N' single space separated integers representing the elements in the array/list.
# Third line contains an integer 'X'.
# Output format : For each test case, print the total number of triplets present in the array/list.
# Output for every test case will be printed in a separate line.

# Sample Input 1:
# 1
# 7
# 1 2 3 4 5 6 7 
# 12
# Sample Output 1:
# 5
# Sample Input 2:
# 2
# 7
# 1 2 3 4 5 6 7 
# 19
# 9
# 2 -5 8 -6 0 5 10 11 -3
# 10
# Sample Output 2:
# 0
# 5
# Explanation for Input 2: Since there doesn't exist any triplet with sum equal to 19 for the first query, we print 0.
#For the second query, we have 5 triplets in total that sum up to 10. They are, (2, 8, 0), (2, 11, -3), (-5, 5, 10), (8, 5, -3) and (-6, 5, 11)

**** SOLUTION ****

from sys import stdin

def findTriplet(arr, n, x) :
    #Your code goes here
    #return your answer
    count = 0
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if arr[i] + arr[j] + arr[k] == x:
                    count =count+1
    return count

    
#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

#main
t = int(stdin.readline().strip())

while t > 0 :
    arr, n = takeInput()
    x = int(stdin.readline().strip())
    print(findTriplet(arr, n, x))
    t -= 1
