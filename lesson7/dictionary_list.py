# ----------------------------------------
# Created by Serhii Skliarov
#
# Version      Date     Info
# 1.0          2021     Init version
#
#-----------------------------------------

enemy = {
    "loc_x": 70,
    "loc_y": 50,
    "color": "green",
    "health": 100,
    "name": "zorg",
    }

all_enemis = []

for x in range (0, 3):
    all_enemis.append(enemy.copy())


for enem in all_enemis:
    print(enem)

all_enemis[2]["health"] = 30
all_enemis[1]["loc_x"] += 15
all_enemis[0]["name"] = "dzeng"

for enem in all_enemis:
    print(enem)