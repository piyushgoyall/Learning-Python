# WAP to input a matrix and calculate sum of each row.

n=int(input())
li1=[[int(x) for x in input().split()]for i in range(n)]
for i in range(len(li1)):
    sum=0
    for j in range(len(li1[i])):
        sum+=li1[i][j]
    print(sum)
    
**** OUTPUT ****

3
1 2 3 4 5
1 2 3
1 2
15
6
3
