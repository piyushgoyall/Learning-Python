#9 Write a Python program to remove the nth index character from a nonempty string.

non = input().strip()
n = int(input())
n1 = ""
for i in range(len(non)):
    if i != n:
        n1 = n1 + non[i]
print(n1)

# OR

print(non[0:n]+non[n+1:])

# **** OUTPUT ****

# startling
# 5
# starting
# starting
