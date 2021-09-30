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
    "name": "zorg"
}

print("Loc X: " + str(enemy["loc_x"]) + " Loc Y: " + str(enemy["loc_y"]))
print("Name: " + enemy["name"])

""" enemy["rank"] = "admiral"
print(enemy)

del enemy["color"]
print(enemy) """

enemy["loc_x"] = enemy["loc_x"] + 40
enemy["health"] = enemy["health"] - 30
if enemy["health"] < 80:
    enemy["color"] = "red"

print(enemy)

print(enemy.keys())
print(enemy.values())