# ----------------------------------------
# Created by Serhii Skliarov
#
# Version      Date     Info
# 1.0          2021     Init version
#
#-----------------------------------------

def create_record(name, tel, addr):
    """Create record"""
    record = {
        "name": name,
        "phone": tel,
        "adress": addr
    }

    return record

user1 = create_record("Vasya", "+38099", "Kiev")
user2 = create_record("Yura", "+38055", "Kiev")

print(user1)
print(user2)

def give_avard(medal, *persons):
    """Give medal to persons"""
    for person in persons:
        print("Person " + person.title() + " take medal " + medal)
    
give_avard("Gold medal", "Vasya", "Petya")
give_avard("Silver medal", "Alex", "Sachino")