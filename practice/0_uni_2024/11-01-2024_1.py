my_nums = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda num: num%2 == 0,my_nums)))


# my_nums = [1,2,3,4,5]
# print(list(map(lambda num: num**2,my_nums)))


# sq = lambda num: num**2
# print(sq(5))



# def check_even(num):
#     return num % 2 == 0
# nums = [0,1,2,3,4,5,6,7,8,9,10]
# print(filter(check_even,nums))


# def splicer(mystring):
#     if len(mystring) % 2 == 0:
#         return 'even'
#     else:
#         return mystring[0]
# mynames = ['john','cindy','emily','penny','rose']
# print(list(map(splicer, mynames)))


# def square(num):
#     return num**2
# my_nums = [1,2,3,4,5]
# print(map(square,my_nums))



# def myFunc(**kwargs):
#     if 'fruit' in kwargs:
#         print(f"My favourite fruit is {kwargs['fruit']}") 
#     else:
#         print("I don't like fruits")
# myFunc(fruit = 'pineapple')


# def myFunc(*args):
#     return sum(args)*.05
# print(myFunc(40,60,20))


# # check occurrence of each element
# def check_occur(list1, i):
#     check = 0
#     for x in list1:
#         if x == i:
#             check = check + 1
#     return check

# list1 = [1, 2, 3, 1, 2, 1]
# already_out = set()

# for i in list1:
#     if i not in already_out:
#         print(i, "occurs", check_occur(list1, i), "times")
#         already_out.add(i)



# def add_num(num1,num2):
#     return num1+num2
# print(add_num(1,2))


# def greeting(name):
#     print(f'Hello {name}')
# greeting('Jose')


# # if we write say_hello OUTPUT is : <function__main__.say_hello>

# def say_hello():
#     print("Hello")
# say_hello()


# list = [1,2,3,4,5,7,1,2,2]
# help(list)