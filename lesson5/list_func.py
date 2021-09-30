# ----------------------------------------
# Created by Serhii Skliarov
#
# Version      Date     Info
# 1.0          2021     Init version
#
#-----------------------------------------

cars = ["Reno", "Seat", "Skoda", "Lada", "Toyota"]

for car in cars:
    print(car.upper())

for car in range (1, 3):
    print(car)

num_list = list(range(0, 10))

num_list.sort(reverse=True)

print(num_list)
for x in num_list:
    x= x * 2
    print(x)


print("Max number: " + str(max(num_list)) + " Min number: " + str(min(num_list)))
print(sum(num_list))

mycars = cars[:4]
print(mycars)

mycars = cars[-3:-1]
print(mycars)

mycars = cars[:]
cars.append("Volvo")
print(cars)
print(mycars)