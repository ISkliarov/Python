# ----------------------------------------
# Created by Serhii Skliarov
#
# Version      Date     Info
# 1.0          2021     Init version
#
#-----------------------------------------

class Hero():
    """ Class to create hero for Game """
    def __init__(self, name, level, race):
        """ Initiate Hero"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self):
        """ Print all parameters of tyis Hero """
        description = (self.name + " " + "Level is: " + str(self.level) + " " + "Race is: " + self.race + " " + "Health: " + str(self.health)).title()
        print(description)

    def level_up(self):
        """ Upgrade level of hero"""
        self.level = self.level + 1

    def move(self):
        """ Start moving hero """
        print("Hero " + self.name + " Start moving...")

    def set_health(self, new_health):
        self.health = new_health