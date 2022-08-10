def adding(lista = []):
    new_member = input("Enter new avenger: ")
    lista.append(new_member)

def remove(lista = []):
    rejected = input("Enter avenger to be removed: ")
    if rejected in lista:
        lista.remove(rejected)

def printing(lista = []):
    for hero in lista:
        print(f"The mighty {hero} is part of Avengers!")

def run():
    avengers = []
    while True:
        opt = int(input("Avengers, Assemble!\n\n1-Add a new avenger\n2-Remove an avenger\n3-Check on the team\n9-Exit\nOption: "))
        if opt == 1:
            adding(avengers)
        elif opt == 2:
            remove(avengers)
        elif opt == 3:
            printing(avengers)
        elif opt == 9:
            break
        else:
            print("No such option exists! Try Again. Dummy.")
    

run()
