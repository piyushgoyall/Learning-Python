# Print the following pattern for the given number of rows.
# Pattern for N = 5
# E
# DE
# CDE
# BCDE
# ABCDE

n=int(input())
Row=1
while Row<=n:
    Col=1
    char=ord('A')+n-Row
    while Col<=Row:
        print(chr(char+Col-1),end="")
        Col+=1
    print()
    Row+=1
