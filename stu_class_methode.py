class Student:
  #create student class
  school ="nobel arrivo"
#add name,marks

  def __init__(self,name,marks):
    self.name=name
    self.marks=marks
    #store value
  
  def display(self):
    print("name:",self.name)
    print("marks:",self.marks)
    print("school:",self.school)
  #static method
  @staticmethod
  def info():
    print("Good morning")
  #class method
  @classmethod
  def change_school(cls,new_school):
    cls.school=new_school
  
s1=Student("bhavesh",90)
s2=Student("keval",80)

s1.display()
s2.display()
Student.info()
