# Python program to enter basic salary and calculate total salary according to the following conditions :
# salary <= 10000 then hra = 5% and da = 7%
# salary > 10000 then hra = 7% and da = 10%

bs = int(input("Enter basic salary : "))
print()

if bs <= 10000:
    hra = (5*bs)/100
    da = (7*bs)/100
    ts = bs + hra + da
    print("Basic salary : ",bs,"\n\nHRA : ",hra,"\n\nDA : ",da,"\n\nTotal salary : ",ts)

else:
    hra = (7*bs)/100
    da = (10*bs)/100
    ts = bs + hra + da
    print("Basic salary : ",bs,"\n\nHRA : ",hra,"\n\nDA : ",da,"\n\nTotal salary : ",ts)
