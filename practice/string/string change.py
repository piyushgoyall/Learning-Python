#5 Write a Python function to create the HTML string with tags around the word(s).
# Sample function and result :
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'

create = input()
tag = input()
print("<"+tag+">"+create+"</"+tag+">")

# **** OUTPUT ****

# Python Tutorial
# b
# <b>Python Tutorial</b>
