

cites = ["New York", "Moscov", "New Daly", "Toronto", "London"]

##print(len(cites))
print(cites[-2].upper())
cites[2] = "Tula"

print(cites)

cites.append("Kursk")
cites.insert(1, "Kyiv")

print(cites)

del cites[2]

print(cites)

cites.remove("Tula")
deletet_city = cites.pop()
print(deletet_city)

print(cites)

cites.sort(reverse=True)
cites.reverse()

print()