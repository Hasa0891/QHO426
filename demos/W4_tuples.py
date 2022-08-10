#Declare a tuple
x = ("Piotr", 88, False) 
y = tuple(["Garry", 35, True])
#Print tuples
print(x)
print(y)
print(x[1])
#Cannot change data inside of a tuple!
#y[0] = "Harry"

#Concatenate tuples
z = x + y
print(z)
print(y)
print(x)
#Using min and max on tuples
h = (5, 2, 34, 88, 77, 10, -5, -8)
print(max(h))