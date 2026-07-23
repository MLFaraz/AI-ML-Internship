class Intern:
    def __init__(self, id, name, dept):
        self.id = id
        self.name = name
        self.dept = dept
        self.tasks = {}

class InternSystem:
    def __init__(self):
        self.interns = {}
        self.load()

    def load(self):
        try:
            f = open("interns.txt", "r")
            for line in f:
                parts = line.strip().split(",")
                if len(parts) >= 3:
                    i = Intern(parts[0], parts[1], parts[2])
                    if len(parts) > 3:
                        for j in range(3, len(parts), 2):
                            if j + 1 < len(parts):
                                i.tasks[parts[j]] = parts[j + 1]
                    self.interns[i.id] = i
            f.close()
        except:
            pass

    def save(self):
        f = open("interns.txt", "w")
        for i in self.interns.values():
            line = i.id + "," + i.name + "," + i.dept
            for t, s in i.tasks.items():
                line += "," + t + "," + s
            f.write(line + "\n")
        f.close()

    def add(self):
        id = input("ID: ")
        if id in self.interns:
            print("ID already exists")
            return
        name = input("Name: ")
        dept = input("Department: ")
        self.interns[id] = Intern(id, name, dept)
        self.save()
        print("Intern added")

    def view(self):
        if not self.interns:
            print("No interns")
            return
        for i in self.interns.values():
            print("ID:", i.id, "Name:", i.name, "Dept:", i.dept)
            if i.tasks:
                print("  Tasks:")
                for t, s in i.tasks.items():
                    print("    ", t, "-", s)

    def search(self):
        q = input("Enter ID or Name: ").lower()
        found = False
        for i in self.interns.values():
            if q == i.id.lower() or q == i.name.lower():
                print("ID:", i.id, "Name:", i.name, "Dept:", i.dept)
                found = True
        if not found:
            print("Not found")

    def assign_task(self):
        id = input("Intern ID: ")
        if id not in self.interns:
            print("Intern not found")
            return
        t = input("Task name: ")
        self.interns[id].tasks[t] = "Pending"
        self.save()
        print("Task assigned")

    def update_task(self):
        id = input("Intern ID: ")
        if id not in self.interns:
            print("Intern not found")
            return
        print("Tasks:", list(self.interns[id].tasks.keys()))
        t = input("Task name: ")
        if t not in self.interns[id].tasks:
            print("Task not found")
            return
        s = input("Status (Pending/In Progress/Completed): ")
        self.interns[id].tasks[t] = s
        self.save()
        print("Status updated")

    def delete(self):
        id = input("Intern ID to delete: ")
        if id in self.interns:
            del self.interns[id]
            self.save()
            print("Deleted")
        else:
            print("Not found")

sys = InternSystem()
while True:
    print("\n1. Add Intern")
    print("2. View All Interns")
    print("3. Search Intern")
    print("4. Assign Task")
    print("5. Update Task Status")
    print("6. Delete Intern")
    print("7. Exit")
    c = input("Choice: ")

    if c == "1":
        sys.add()
    elif c == "2":
        sys.view()
    elif c == "3":
        sys.search()
    elif c == "4":
        sys.assign_task()
    elif c == "5":
        sys.update_task()
    elif c == "6":
        sys.delete()
    elif c == "7":
        break
    else:
        print("Invalid choice")
