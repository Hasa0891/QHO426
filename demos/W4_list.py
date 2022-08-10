#Declare an empty list
bleh = []
meh = list()
#Declare a non-empty list
yummy = ["Pizza", "Sarmale", 'Ice Cream', "Carnati"]
#Print entire list
print(yummy)
#Print a single item
print(yummy[2])
#Print some items
print(yummy[:2])
#Add elements to our list (expand it) - adding at the end of the list
print(bleh)
bleh.append("Pierogi")
bleh.append("Steak")
bleh.append("Liver")
bleh.append("Horse Meat")
print(bleh)
#Add multiple items to a list
for i in range (2):
    bleh.append("Salad")
print(bleh)
bleh.extend(["Racitura", "Soup", "Cat"])
print(bleh)
#Insert items at specific positions on the list
bleh.insert(1, "Cabbage")
bleh.insert(4, "Mushed Peas")
print(bleh)
#Remove item from list
if "Pierogi" in bleh:
    bleh.remove("Pierogi")
if "Horse Meat" in bleh:
    bleh.remove("Horse Meat")
if "Potatoes" in bleh:
    bleh.remove("Potatoes")
print(bleh)
#Remove item by index
x = bleh.pop(1)
print(bleh)
print(x*8)
#Alternative way of deleting item via index
del bleh[2]
print(bleh)
#Extending list by another list
yummy.extend(bleh)
print(yummy)
print(bleh)
#Mutating a list
yummy[4] = "Hamburger"
yummy[1] = 67894
print(yummy)
#Check a list for particular data type/traverse a list
lista = ["Fred", 56, True, "Piotr", -4.8, "Ham", 89, False]
for item in lista:
    if isinstance(item, str) or isinstance(item, float):
        print(item, end = " ")