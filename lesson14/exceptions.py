# ----------------------------------------
# Created by Serhii Skliarov
#
# Version      Date     Info
# 1.0          2021     Init version
#
#-----------------------------------------
import sys

filename = "Names.txt"

while True:
    try:
        print("Inside TRY")
        myfile = open(filename, mode='r', encoding="utf-8")
    except Exception:
        print("Inside Exception")
        print("Error Found")
        print(sys.exc_info()[1])
        filename = input("Enter correct file name: ")
    else:
        print("Inside ELSE")
        print(myfile.read())
        sys.exit()

    print("------ EOF ------")