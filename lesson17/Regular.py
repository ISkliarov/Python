# ----------------------------------------
# Created by Serhii Skliarov
#
# Version      Date     Info
# 1.0          2021     Init version
#
#-----------------------------------------
import re

input_filename = "tamplate.txt"
result_filename = "result.txt"

inputfile = open(input_filename, mode='r', encoding="utf-8")
resultfile = open(result_filename, mode='w', encoding="utf-8")
mytext = inputfile.read()

lookfor = r"[\w.]+@(?!intel.com)[A-Za-z-.]+"

results = re.findall(lookfor, mytext)

for item in results:
    print(item)
    resultfile.write(item + "\n")

print("Total: " + str(len(results)))
