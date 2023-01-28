#9 Write a program that display following output:

# SHIFT
# HIFTS
# IFTSH
# FTSHI
# TSHIF
# SHIFT

n=input().strip()
for i in range(len(n)):
    n=n[1:]+n[0]
    print(n)
    
# **** OUTPUT ****

# SHIFT
# HIFTS
# IFTSH
# FTSHI
# TSHIF
# SHIFT
