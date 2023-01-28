# Wap to calculate factorial of a number using function.

def fact(num):
    pro = 1
    for i in range(1,num+1,1):
        pro = pro*i
    return pro

n = int(input())
a = fact(n)
print("Factorial of {} is : {}".format(n,a))
