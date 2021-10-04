# ----------------------------------------
# Created by Serhii Skliarov
#
# Version      Date     Info
# 1.0          2021     Init version
#
#-----------------------------------------
import sys
import os

x = len(sys.argv)

if x > 1:
    if sys.argv[1] == "/y":
        print("Help Requsted")
        print("Ussage of program arguments.py: return entered arguments")

    print("Argument entered: " + str(sys.argv[2:]))
else:
    print("Argument NOT PROVIDED")

sys.exit(2)
os.system("touch python_created.txt")
os.system("echo 'Hello))' > python_created.txt")
os.system("cat python_created.txt")
#os.mkdir("MyDir")
