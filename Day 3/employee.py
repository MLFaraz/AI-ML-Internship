class Employee:
    def __init__(self, name, basic, hra, da):
        self.name = name
        self.basic = basic
        self.hra = hra
        self.da = da

    def salary(self):
        return self.basic + self.hra + self.da

    def show(self):
        print("Name:", self.name)
        print("Monthly Salary:", self.salary())

e = Employee("Bob", 30000, 5000, 2000)
e.show()
