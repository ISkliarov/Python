# ----------------------------------------
# Created by Serhii Skliarov
#
# Version      Date     Info
# 1.0          2021     Init version
#
#-----------------------------------------

from urllib import request
import sys

myUrl = "https://dl.k8s.io/release/v1.22.0/bin/windows/amd64/kubectl.exe"
myFile = "/home/sskliarov/Projects/Python/lesson18/kubectl.exe"

try: 
    print('Start Downloading file from: ' + myUrl)
    request.urlretrieve(myUrl, myFile)
except Exception:
    print("Achtung!!!")
    print(sys.exc_info())
    exit

print("File Downloaded and saved at: " + myFile)