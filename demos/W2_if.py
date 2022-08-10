name = input("Enter your name: ")
#len() - function that returns the length of an item, you put inside of it

if len(name) > 8:
    print("Your name is very long. Please tell me a nickname: ")
    name = input()
elif len(name) <= 3:
    print("Your name is super short")
elif name.upper() == "MARTHA":
    print("Why did you say that name? (in Batman's voice)")
else:
    print("You have a meh name!")
    
print(f"Welcome {name}!")