# ----------------------------------------
# Created by Serhii Skliarov
#
# Version      Date     Info
# 1.0          2021     Init version
#
#-----------------------------------------

""" def print_hello():
    print("Congratulation? wish you all the best!!!!")
    print("______ TADA ________")

def message(name):
    print("This is message by: " + name)

def summa(a, b):
    s = a + b
    return s


#-----------------------------------------------------

print("-------------------------------------------")
print_hello()
message("Sergii")

x = summa(10, 30)
print(x) """

def factorial(a):
    """ ---- Calculate factorial of number x ---- """
    fact = 1
    for i in range (1, a + 1):
        fact = fact * i
    return fact

for i in range(1, 10):
    print(str(i) + "!\t = " + str(factorial(i)))