# Python: Sum of number digits in List

p = [int(d) for d in input().split()]
summ = []
for digit in p:
    sum = 0
    while digit > 0:
        rem = digit%10
        sum = sum+rem
        digit = digit//10
    summ.append(sum)
print(summ)

# **** OUTPUT ****


# 121 67 688 6358 568 737 376
# [4, 13, 22, 22, 19, 17, 16]
