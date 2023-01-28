# Print table of a number using function.

def table(num):
    pro = 0
    for i in range(1,11,1):
        pro = num*i
        print(num,"*",i,"=",pro)
    
n = int(input())
table(n)    
