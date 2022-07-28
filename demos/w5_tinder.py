def interests():
    print("Enter all your interests, one after the other and enter \"stop\" when done ")
    s1 = set()
    while True:
        interest = input()
        if interset.lower() == "stop":
          break
        else:
          s1.add(interest)
    return s1

print(interest())