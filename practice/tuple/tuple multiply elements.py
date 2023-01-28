# Multiply each and every element of a tuple with a number.

t = (1,2,3,4,5,6,7,8,9)
u = tuple(5*ele for ele in t)
print(u)

**** OUTPUT ****

(5, 10, 15, 20, 25, 30, 35, 40, 45)
