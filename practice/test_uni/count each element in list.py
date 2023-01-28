# Input a list and print occurence of each element in the list.

li1 = [int(x) for x in input().split()]
li2 = []
for i in li1:
    if i not in li2:
        li2.append(i)
for i in li2:
    count = 0
    for j in li1:
        if i == j:
            count += 1
    print(i,count)
    
    **** OUTPUT ****
    
1 2 3 4 5 6 7 8 9 1 2 5 3 2 6 7 8 9 0 8 5 6 
1 2
2 3
3 2
4 1
5 3
6 3
7 2
8 3
9 2
0 1
