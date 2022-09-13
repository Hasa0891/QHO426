#The class Person which will be a blueprint for my objects to store information about humans/people
class Person:

#Class Attribute -> attribute/feature accessible for all objects of the class
    MAX_W = 150
    
#Static Method -> Utility function, that does not require an object of our class to be instantiated
    def is_mature(age):
       if age >= 18:
           return "Person is mature"
       else:
           return "Person is immature"
    
#Initialiser/Constructor -> function that is automatically invoked immediately when an object is created (-magic method)
    #Initialiser of ANY class has the same name
    #"DUNDER" -> Double Underscore
    def __init__(self, name = "", age = 0, job = "Unemployed", weight = 2):
        #Below are instance attributes (features of any Person)
        self.name = name
        self.age = age
        self.job = job
        if weight <= Person.MAX_W:
            self.weight = weight
        else:
            self.weight = Person.MAX_W

    #Magic method str, which provides the "informal" object representation. It is invoked automatically when object goes into print() function
    def __str__(self):
        return f"Person {self.name} is {self.age} years old. They work as {self.job} and currently weights {self.weight} kg"

    #Magic method repr, which provides the "formal" object representation. "Formal" representation is how yo uwant to store your object.
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age}, job={self.job})"

    #Method - function attached to a specific data type
    #Instance method -> it applies to a specific instance of a class
    def eat(self, food, w):
        print(f"{self.name} have eaten {food}")
        self.weight += w
        print(f"{self.name} now weights {self.weight}kg")

    def exercise(self, burned):
        self.weight -= burned
        print(f"{self.name} has exercised and now weights {self.weight}kg")


if __name__ == "__main__":
    p1 = Person("Tom")
    print(type(p1))
    p2 = Person("Beth", 25, "Accountant", 72)
    print(repr(p1))
    print(repr(p2))
    print(f"Person called {p1.name} is {p1.age} years old and weight {p1.weight}kg")
    print(f"Person called {p2.name} is {p2.age} years old and weight {p2.weight}kg")
    p2.eat("Spaghetti", 2.3)
    p2.eat("Sandwich", 0.3)
    p2.exercise(1.5)
    p1.eat("Pizza", 1.2)
    print(Person.is_mature(18))
    print(Person.is_mature(p1.age))
    print(Person.is_mature(p2.age))