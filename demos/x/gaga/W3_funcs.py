#Definition of a new function - specifying what it is and what it does, so that it can be used later
#Parameter - data given/injected into a function
#Default Parameter - value assumed by a parameter if no argument is given
def t_area(b=2, h=1):
    area = b*h*0.5
    return area

def run():
#Call the function to make it run!
    total_area = t_area() + t_area(10, 8) + t_area(9)
    print(total_area)
    print(t_area(7,5))
    return 1