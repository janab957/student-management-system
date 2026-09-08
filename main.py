from numpy import True_
from logging import NullHandler
from contextlib import nullcontext
class Student:

  stu_dict={}

  def __init__(self, name, grades):
    self.name=name
    self.grades=grades

  def add(name):
    try:
      stu_dict[name]=[]
      return True
    except NullHandler:
      print("Invalid name!")
      return False

  def rem(name):
    try:
      del stu_dict.keys(name)
      return True
    except KeyError:
      print("Name not Found!")
      return False

  def view():
    with open ("students.txt", "r") as file:
      for i in file:
        name, grades = i.split(":")
        print ("Name: ", name)
        print("Grades", grades)

  def find(name):
    try:
      if name in stu_dict.keys():
        print("Name: ", name, "\n Grades: ", stu_dict[name])
    except KeyError:
      print("Name doesn't exist!")

  def add_grade(name, grade):
    try:
     stu_dict[name].append(grade)
     return True

    except ValueError:
      print("Invalid Input!")
      return False

  def csa(name):
    sums=0
    sav
    try:
      if name in stu_dict.keys():
        sums+=stu_dict[name].sum()
        sav=sums/len(stud_dict[name])
        return sav

    except KeyError:
        print("Name doesn't exist!")
    except NullHandler:
      print("Student has no grade yet!")

  def cca():
    try:
      sums=0
      for i in stu_dict:
        sums+=stu_dict.values.sum()

      ca= sums/len(stu_dict)

      print("Calss Average: ", ca)

    except NullHandler:
      print("no records yet!")




print("======== Student Management System ========")

print("\n\n1. Add Student\n2. Remove Student\n3. View Students\n4. Find Student\n5. Add Grade\n6. Calculate Student Average\n7. Calculate Class Average\n8. Exit\n\n")

opt=int(input("Choose: "))

while True:

  if opt==1:
    name=input("Enter the name: ")
    result=Student.add(name)
    if result==True:
      print("Student Added!")

  elif opt==2:
    name=input("Enter the name: ")
    result=Student.rem(name)
    if result==True:
      print("Student removed!")

  elif opt==3:
    Student.view()

  elif opt==4:
    name=input("Enter the name: ")
    Student.find(name)

  elif opt ==5:
    name=input("Enter the name: ")
    grade=input("Enter the grade: ")

    result = Student.add_grade(name, grade)

    if result == True:
      print("grade was added successfully!")

  elif opt==6:
    name=input("Enter the name: ")
    result=Student.csa(name)
    print("Student Average", result)

  elif opt==7:
    Student.cca()

  elif opt==8:
    with open ("Students.txt", "w") as file:
      for key, value in stu_dict.items():
        file.write(i.key(),":", i.value())
      break
      print("Exiting the program!")



