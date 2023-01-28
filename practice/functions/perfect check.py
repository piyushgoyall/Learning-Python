# Wap to check if a number is perfect or not using function. Return true if perfect and false if not.

def perfect_check(num):
    sum = 0
    for x in range(1, num):
        if num % x == 0:
            sum = sum + x
    return sum == num

n = int(input())
a = perfect_check(n)
print(a)
