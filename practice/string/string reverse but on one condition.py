#9 Write a Python function to reverses a string if it's length is a multiple of 4.

four = input().strip()
if len(four)%4 == 0:
    s = ""
    for i in four:
        s = i+s
    print(s)
else:
    print("String length is not a multiple of 4")
    
# **** OUTPUT ****

# qwer1234
# 4321rewq
