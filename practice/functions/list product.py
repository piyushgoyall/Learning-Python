# Wap to multiply all the numbers in a list using function.

def multiply(num):
    pro = 1
    for i in num:
        pro = pro*i
    return pro
        

print(multiply((8,2,3,-1,7)))
