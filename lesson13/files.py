# ----------------------------------------
# Created by Serhii Skliarov
#
# Version      Date     Info
# 1.0          2021     Init version
#
#-----------------------------------------

input_file = "./pass.txt"
outputefile = "./output.txt"

password_tolook = "usa"

myfile = open(input_file, mode="r", encoding="utf-8")
myfile_output = open(outputefile, mode="a", encoding="utf-8")

for num, line in enumerate(myfile, 1):
    if password_tolook in line:
        print("Line # " + str(num) + " Pass:  " + line.strip())
        myfile_output.write("Found password: " + line)

print(myfile.read())

myfile.close()
myfile_output.close()