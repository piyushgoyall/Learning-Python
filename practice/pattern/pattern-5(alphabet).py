# For n = 5 print the following pattern.

# A B C D E 
# A B C D E 
# A B C D E 
# A B C D E 
# A B C D E 

n = int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        char = chr(ord('A')+j-1)
        print(char,end=" ")
    print()
