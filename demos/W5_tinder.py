def interests():
    print("Enter all your interests, one after the other and enter \"stop\" when done ")
    s1 = set()
    interest = ""
    while interest.lower() != "stop":
        interest = input()
        if interest.lower() != "stop":
            s1.add(interest)
    return s1

def tinderDaSecond():
    print("First Person: ")
    p1 = interests()
    print("Second Person: ")
    p2 = interests()
    common = p1.intersection(p2)
    if len(common) >= 3:
        print(f"Yay - you are a match made in heaven! You have {len(common)} common interests")
    else:
        print("Oh no - there is no way it will work out :(")

tinderDaSecond()def interests():
    print("Enter all your interests, one after the other and enter \"stop\" when done ")
    s1 = set()
    interest = ""
    while interest.lower() != "stop":
        interest = input()
        if interest.lower() != "stop":
            s1.add(interest)
    return s1

def tinderDaSecond():
    print("First Person: ")
    p1 = interests()
    print("Second Person: ")
    p2 = interests()
    common = p1.intersection(p2)
    if len(common) >= 3:
        print(f"Yay - you are a match made in heaven! You have {len(common)} common interests")
    else:
        print("Oh no - there is no way it will work out :(")

tinderDaSecond()