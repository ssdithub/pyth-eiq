class Person:
    def __init__(self, name,age):
        self.name = name
        self.age=age
    def showinfo(self):
        print(f"name:{self.name}, Age:{self.age}")

class Student(Person):
    def __init__(self, name,age,grade):
        super().__init__(name,age)  # call parent class constructor
        self.grade = grade

    def showinfo(self):
        print(f"name:{self.name}, Age:{self.age}, grade: {self.grade}")

stu1 = Student("Saakshi",21, 7)
stu1.showinfo()
