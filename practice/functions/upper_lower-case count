# Wap to count total number of upper and lower case letters using function.

def check(string):
    u = 0
    l = 0
    w = len(string)
    for i in range(w):
        if string[i] == " ":
            continue
        elif (ord(string[i]) >= 97 and ord(string[i]) <= 122 ):
            l = l+1
        elif (ord(string[i]) >= 65 and ord(string[i]) <= 90 ):
            u = u+1
    print()     
    print("Total lowercase : {}".format(l))
    print()
    print("Total uppercase : {}".format(u))
    
string = input()
check(string)
