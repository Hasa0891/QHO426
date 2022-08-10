age = int(input("Enter age: "))
ch = int(input("Enter number of children: "))

if age > 25 and ch > 0 and age <= 55:
    print("You are a parent. Yay!")
    print(f"Next year you will be {age+1} years old")
elif age > 55 and ch > 0:
    print("Your children will hopefully support you when you get older")
elif age < 18 or ch == 0:
    print("There is still plenty of time to have a child, if you want!")
else:
    print("You are not so young :(")
    print("We are going to live a long live anyway!")
    