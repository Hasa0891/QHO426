def box(word):
    length = len(word)
    print("#"*(length+4))
    print("# " + word + " #")
    print("#"*(length+4))

def low(word):
    print(word.lower())

def up(word):
    print(word.upper())

def mirror(word):
    print(word, "|", word[::-1])

def repeat(word):
    n = int(input("How many times to repeat: "))
    for i in range (n):
        if i % 2 == 0:
            up(word)
        else:
            low(word)

def run():
    w = input("Enter a word: ")
    print("Choose an option:\n1-Box\n2-Lower Case\n3-Upper Case\n4-Mirror\n5-Repeat")
    opt = int(input())
    if opt == 1:
        box(w)
    elif opt == 2:
        low(w)
    elif opt == 3:
        up(w)
    elif opt == 4:
        mirror(w)
    elif opt == 5:
        repeat(w)
    else:
        print("No such option")
    

run()

#Slicing - act of separating/accessing individual items of a list OR characters in a string
#Slice using [start, end, step]
#word = "This is Sparta!"
#print(word[::-1])