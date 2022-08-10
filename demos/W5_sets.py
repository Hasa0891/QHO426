#Initialise an empty set
s = set()
#Initialise non-empty set
colours = {"blue", "red", "yellow", "purple"}
print(colours)
#Adding elements to a set
colours.add("green")
print(colours)
#Remove item from a set
if "red" in colours:
    colours.remove("red")
if "turqoise" in colours:
    colours.remove("turqoise")
print(colours)
#Sets are heterogenous and duplicates are not allowed
colours.add(99)
colours.add(False)
colours.add("blue")
print(colours)
#Check membership
if "blue" in colours:
    print("Yay - I love blue!")
else:
    print("You need some blue in your life mate!")

c = {"black", "white", "cyan", "blue", "red", "pink", "yellow", "orange", "green", "coquelicot"}

#Union - join two sets together, not keeping duplicates (each element included once)
c2 = colours.union(c)
print(f"c is {c}")
print(f"c2 is {c2}")
print(f"colours is {colours}")
#Intersection - looking at "common" values/elements of 2 collections
c3 = colours.intersection(c)
print(f"c3 is {c3}")
#Difference - keep elements of one set that are NOT part of the other
c4 = colours.difference(c)
c5 = c.difference (colours)
print(f"c4 is {c4}")
print(f"c5 is {c5}")