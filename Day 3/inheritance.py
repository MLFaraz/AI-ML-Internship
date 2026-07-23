class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Student(Person):
    def __init__(self, name, age, roll):
        super().__init__(name, age)
        self.roll = roll

    def show(self):
        super().show()
        print("Roll:", self.roll)

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def show(self):
        super().show()
        print("Subject:", self.subject)

s = Student("Tom", 20, 12)
t = Teacher("Jerry", 35, "Math")
s.show()
print()
t.show()
