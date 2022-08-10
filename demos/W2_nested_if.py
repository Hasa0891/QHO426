salary = float(input("Enter Salary: "))
years = int(input("Enter number of years: "))

if years > 2:
    if salary < 25000:
        salary *= 1.1 
        print(f"Your new salary is £{salary:.2f}")
    else: 
        salary += 100
        print(f"Your new salary will be £{salary:.2f}")
elif years >= 1:
    print("No salary increase for you :(")
else:
    if salary < 20000:
        print("Oopsie! Your salary should be £20000")
        salary = 20000
print("Let us work for the good of the company!")