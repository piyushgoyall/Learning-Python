# Input a line separated list and find the pair of elements with maximum sum.

N = int(input())
neww = []
for x in range(0,N):
    ele = int(input())
    neww.append(ele)
maximum = -2**31
for i in range(len(neww)):
    for j in range(i+1,len(neww)):
        if neww[i]+neww[j] > maximum:
            maximum = neww[i]+neww[j]

for i in range(len(neww)):
    for j in range(i+1,len(neww)):
        if neww[i]+neww[j] == maximum:
            print(neww[i],neww[j])
            break
            
**** OUTPUT ****

10
1
2
5
9
7
2
3
0
1
5
9 7
