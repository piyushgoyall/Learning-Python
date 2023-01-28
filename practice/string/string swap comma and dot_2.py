# 8. Write a Python program to swap comma and dot in a string.  

n=input().strip()
s=0
e=len(n)-1
while s<e:
    while s<len(n):
        if n[s]=='.':
            break
        s+=1
    
    while e>0:
        if n[e]==',':
            break
        e-=1
    if s<e:
        n=n[:s]+n[e]+n[s+1:e]+n[s]+n[e+1:]
    s+=1
    e-=1
print(n)

# **** OUTPUT ****

# 32.054,23
# 32,054.23
