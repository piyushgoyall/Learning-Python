# import numpy as np
# a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
# b = a[:2, 1:3]
# print(b)


#19jan
import numpy as np
a= np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
#use slicing to pull out the subarray consisting of the first 2 rows 
#and columns 1 and 2; b is the following arrayy of tghe shape(2,2):
#[2:3]
b=a[:2,1:3]   # before comma-->row after comma--> col
c=a[:2,1:4]
d=a[:3,2:3]
e=a[0,1]
f=a[0,1]=99
print(b)
print(c)
print(d)
print(e)
print(a)
a.shape

#a.shape(include tuple) size-->int
import numpy as np
a= np.array([1,2,3])
a.shape
#(3,) , is acoming cause ita a tuple orelse it would take it as a string

t=(3)
type(t)

t=(3,)
type(t)