#2 Write a Python program to count repeated characters in a string. 
# Sample string: "thequickbrownfoxjumpsoverthelazydog"
# Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2

repeat = input()
# r = ""
for i in range(len(repeat)):
    count = 1
    for j in range(i+1,len(repeat)):
        if repeat[i] == repeat[j] and repeat[i] != " ":
            count += 1
            repeat = repeat[:j] + "0" + repeat[j+1:];
    if count > 1 and repeat[i] != "0":
        print(repeat[i]," - ",count)
#     else:
#         r = r+repeat[i]
#     print(r,end=" ")
    
# string = "welcome to the world of python programming";
    
# print("Duplicate characters in a given string: ");  
# for i in range(0, len(string)):  
#     count = 1;  
#     for j in range(i+1, len(string)):  
#         if(string[i] == string[j] and string[i] != ' '):  
#             count = count + 1;  
#             string = string[:j] + '0' + string[j+1:];  
    
#     if(count > 1 and string[i] != '0'):  
#         print(string[i]," - ",count);


# for i in repeat:
#     if i not in r:
#         r += i
# for i in r:
#     count = 0
#     for j in repeat:
#         if i == j:
#             count += 1
#     print(i,count)

# **** OUTPUT ****

# thequickbrownfoxjumpsoverthelazydog
# t  -  2
# h  -  2
# e  -  3
# u  -  2
# r  -  2
# o  -  4
