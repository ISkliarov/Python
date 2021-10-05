# ----------------------------------------
# Created by Serhii Skliarov
#
# Version      Date     Info
# 1.0          2021     Init version
#
#-----------------------------------------

from urllib import request, parse
import sys

myUrl="https://www.google.com/search?"
value = {'q': 'ANDESA Soft'}

myheader = {}
myheader['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36'

try:
    mydata = parse.urlencode(value)
    print(mydata)
    myUrl = myUrl + mydata
    print(myUrl)
    req = request.Request(myUrl, headers=myheader)
    otvet = request.urlopen(req)
    otvet = otvet.readlines()
    for line in otvet:
        print(line)

except Exception:
    print("Error occuared during web request! ")
    print(sys.exc_info()[1])
