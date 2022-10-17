#  Print the following pattern for given number of rows.
#  Input format : Integer N (Total number of rows)
#  Output Format : Pattern in N lines

#  Sample Input : 5
#  Sample Output :
#              5 4 3 2 *
#              5 4 3 * 1
#              5 4 * 2 1
#              5 * 3 2 1
#              * 4 3 2 1

## Read input as specified in the question.
## Print output as specified in the question.


n = int(input())
for i in range(1,n+1,1):
    for j in range(n,0,-1):
        if i == j:
            print("*",end="")
        else:
            print(j,end="")
    print()
