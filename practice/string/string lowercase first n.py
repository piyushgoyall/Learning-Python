#7 Write a Python program to lowercase first n characters in a string.

low = input()
n = int(input())
print(low[:n].lower() + low[n:])
# for i in range(n):
#     x = low.lower()
# print(lower)

# **** OUTPUT ****

# qWERTFDERFDjhgfcvghj
# 8
# qwertfdeRFDjhgfcvghj
