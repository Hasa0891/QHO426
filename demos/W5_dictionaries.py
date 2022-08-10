#Initialise empty dictionary
dictio = {}
d = dict()
#Instantiate non-empty dictionary
phonebook = {"Thomas":77645926, "Aga": 7735491827, "Ghandi": 770628323}
#Print full dictionary
print(phonebook)
#Print/access individual elements
name = input("Who we are going to call?")
print(phonebook[name])
#Zipping two lists together, into a dictionary
names = ["Frank", "July", "Zanyeb"]
ages = [35, 19, 12, 35]
people = dict(zip(names, ages))
print(people)
#Traversing dictionaries - accessing all keys/values/keys+values
for thing in people:
    print(thing)
for thang in people.values():
    print(thang)
for stuff in people.items():
    print(stuff[0], stuff[1])
for k, v in people.items():
    print(f"Person {k} is {v} years old")
