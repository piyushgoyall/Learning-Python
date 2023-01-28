# Wap to reverse a string using function.

def reverse(str):
    s = " "
    for i in str:
        s = i + s
    return s

str = input()
a = reverse(str)
print("Reversed string : ",a)
