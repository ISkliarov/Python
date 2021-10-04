# ----------------------------------------
# Created by Serhii Skliarov
#
# Version      Date     Info
# 1.0          2021     Init version
#
#-----------------------------------------
import json
from json import *
from os import EX_CONFIG

filename = "user_setting.txt"
myfile = open(filename, mode="w", encoding='Latin-1')


player1 = {
    "PlayerName" : "Donald Trump",
    "Score" : 345,
    "Awards" : ["OR", "NV", "NY"] 
}

player2 = {
    "PlayerName" : "Clinton Hillary",
    "Score" : 237,
    "Awards" : ["WI", "TX", "MI"]
}

myplayers = []
myplayers.append(player1)
myplayers.append(player2)

# ------- Save JSON -------------

json.dump(myplayers, myfile)
myfile.close()

# ------- LOAD by JSON ----------

myfile = open(filename, mode='r', encoding='utf-8')
json_data = json.load(myfile)

for user in json_data:
    print("Player Name is: " + str(user["PlayerName"]))
    print("Payer Score is: " + str(user["Score"]))
    print("Player  Awards N1 : " +str(user['Awards'][0]))
    print("Player  Awards N2 : " +str(user['Awards'][1]))
    print("Player  Awards N3 : " +str(user['Awards'][2]))

    print(" _________ END ___________ ")

