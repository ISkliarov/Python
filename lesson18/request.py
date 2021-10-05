# ----------------------------------------
# Created by Serhii Skliarov
#
# Version      Date     Info
# 1.0          2021     Init version
#
#-----------------------------------------

from urllib import request

myUrl = "Http://www.astahov.net"

try:
    print("Inside TRY")
    otvet =request.urlopen(myUrl)
    mytext1 = otvet.readlines()
    mytext2 = otvet.read()
except Exception:
    print("END")
    
else:
    print(otvet)
    for line in mytext1:
        print(line)
