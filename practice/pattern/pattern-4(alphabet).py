# For n = 5 print the following pattern.

# AAAAA
# BBBBB
# CCCCC
# DDDDD
# EEEEE

n = int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        char = chr(ord('A')+i-1)
        print(char,end="")
    print()
