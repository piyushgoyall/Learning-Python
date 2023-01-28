# Python program to check whether the given number is prime or not.

n = int(input())
flag = False
for i in range(2,n,1):
    if n%i == 0:
        flag = True
        break
    
if flag == True:
    print(f"{n} is not a Prime number")
else:
    print(f"{n} is a Prime number")
