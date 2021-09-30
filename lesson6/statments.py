# ----------------------------------------
# Created by Serhii Skliarov
#
# Version      Date     Info
# 1.0          2021     Init version
#
#-----------------------------------------

""" x = 25

if x == 25:
    print("Yes, you right")
else:
    print("No, your wrong")

q_age = input("Enter yoy value: ")
age = int(q_age)
if (age <= 4):
    print("Baby")
elif (age > 4) and (age < 12):
    print("You are kid")
elif(age >= 12) and (age <= 18):
    print("Yong")
else:
    print("You old") """

cars = ["Reno", "Seat", "Skoda", "Lada", "Toyota", "Mercedes"]
premium_car = ["BMW", "Mercedes"]

if "Lada" in cars:
    print("Lada is here")
else:
    print("No Lada in list")

for xx in cars:
    if xx in premium_car:
        print(xx + " in premium cars")
    else:
        print(xx + " is not premium")

