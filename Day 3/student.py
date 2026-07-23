class Student:
    def __init__(self, name, roll, dept):
        self.name = name
        self.roll = roll
        self.dept = dept

    def show(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll)
        print("Department:", self.dept)

s = Student("Alice", 101, "CS")
s.show()
