#10 Write a Python program to change a given string to a new string where the first and last chars have been exchanged.

exchange = input().strip()
print(exchange[-1]+exchange[1:len(exchange)]+exchange[0])

# **** OUTPUT ****

# apple
# epplea
