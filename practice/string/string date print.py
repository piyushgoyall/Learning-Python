# 6. Write a program that reads a string from the user containing a date in the
#  form mm/dd/yyyy. It should print the date in the form March 12, 2021.

date = input()
temp = date.split("/")
month = temp[0]
flag = {'01':"January",'02':"February",'03':"March",'04':"April",'05':"May",'06':"June",'07':"July",'08':"August",'09':"September",'10':"October",'11':"November",'12':"December"}
print(flag[month],temp[1] + ', ' + temp[2])

# ** OUTPUT **

# 11/21/2022
# November 21, 2022


# **** OR ****


date = input()
temp = [int(x) for x in date.split("/")]
month = temp[0]
flag = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
print(flag[month],temp[1],', ',temp[2])

# ** OUTPUT **

# 12/01/2022
# December 1 ,  2022
