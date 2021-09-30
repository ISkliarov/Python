# ----------------------------------------
# Created by Serhii Skliarov
#
# Version      Date     Info
# 1.0          2021     Init version
#
#-----------------------------------------

""" a = input("Enter first number: ")
b = input("Enter second number: ")
sum = int(a) + int(b)

print("Output: " + str(sum)) """

""" message = ""

while message != "pass":
    message = input("Enter Pass: ")
    if message== "pass":
        break
    print("Password not Correct")
print("Password was: " + message) """

mylist = []
msg = ""

while msg != "stop".upper():
    msg = input("Enter message while not \"stop\"")
    mylist.append(msg)

print(mylist)