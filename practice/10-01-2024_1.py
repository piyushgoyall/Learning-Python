var = int(input('Enter something into this box: '))
print(var)
print(type(var))


# # # # GENERATE 10 RANDOM NUMBERS USING RANDINT AND FIND THEIR MAXIMUM

# # # from random import randint
# # # list1 = []
# # # for var in range(0,11):
# # #     list1.append(randint(1,100))
# # # print(list1)
# # # print(max(list1))

# # # # from random import randint
# # # # random_numbers = [randint(1, 100) for i in range(10)]
# # # # print("Generated random numbers:", random_numbers)
# # # # print("Maximum number in the list:", max(random_numbers))


# from random import randint
# print(randint(0,100))


# mylist = [10,20,30,40,50]
# from random import shuffle
# shuffle(mylist)
# print(mylist)


# print('x' in ['x','y','z'])


# index_count = 0
# for letter in 'abcde':
#     # print("At index the letter is ",index_count,letter)
#     # print("At index", index_count, "the letter is ",letter)
#     print("At index {} the letter is {} ".format(index_count,letter)) # {} are called placeholders
#     index_count += 1


# print(list(range(0,101,10)))
# print(list(range(0,11,2)))
# print(list(range(0,11)))


# d = {'k1':1,'k2':2,'k3':3}
# for i in d:
#     print(i, end = " ")

# for k,v in d.items():
#     print(k,v,end=" ")


# list3 = ['aman', 'shikha', 'ram']
# for var in list3:
#     for v in var:
#         print(v, end = " ")
#     print() 


# list2 = [(2,4), (6,8), (10,12)]
# for tup in list2:
#     print(tup, end = " ")


# tup = (1,2,3,4,5)
# for t in tup:
#     print(t, end = " ")