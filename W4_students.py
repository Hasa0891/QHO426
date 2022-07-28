def generate():
    name = input("Enter name: ")
    mrk = int(input("Enter final mark"))
    return name, mrk

def list_students(n):
    student_list = []
    for i in range(n):
        student_list.append(generate())
    return student_list

def avg_mark(lista =[]):
    total = 0
    for tup in lista:
        total = total + tup[1]
    average = total/len(lista)
    return average

def run():
    stud_list = []
    while True:
      opt = int(input("Menu:\n1-Populate list of students\n2-calculate Average mark\n3-Change mark of a student\n4-Exit\nOption:"))
      if opt == 4:
        break
      elif opt == 1:
        num = int(input("Enter number of students: "))
        stud_list.extend(list_students(num))
      elif opt == 2:
        print(f"The average markis {avg_mark(stud_list):.0f}")
      elif opt ==3:
        name = input("Enter name of student: ")
        for student in stud_list:
              if student[0].upper() == name.upper():
                 n_mrk = int(input(f"Enter new mark for {name}: "))
                 stud_list.remove(student)
                 stud_list.insert(0,(name, n_mrk))
      else:
          print("You are an idiot")

run()