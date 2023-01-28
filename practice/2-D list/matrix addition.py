# WAP to input two matrices and calculate their sum.

n=int(input())
li1=[[int(x) for x in input().split()]for i in range(n)]
li2=[[int(x) for x in input().split()]for i in range(n)]
new=[[0 for j in range(len(li1[i]))]for i in range(n)]
for i in range(len(li1)):
    for j in range(len(li1[i])):
        new[i][j]+=li1[i][j]+li2[i][j]
print(new)

**** OUTPUT ****

2
1 2 3 4 5 
1 2 3 4
1 2 3 4 5
1 2 3 4
[[2, 4, 6, 8, 10], [2, 4, 6, 8]]
