#6 Write a Python function to insert a string in the middle of a string.
# Sample function and result :
# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}

insert = input()
mid = input()
print(mid[:(len(mid)//2)]+insert+mid[(len(mid)//2):])

# **** OUTPUT ****

# python
# [[]]
# [[python]]
