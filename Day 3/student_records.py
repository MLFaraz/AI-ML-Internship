while True:
    print("1. Add Record")
    print("2. View Records")
    print("3. Exit")
    c = input("Choice: ")

    if c == "1":
        name = input("Name: ")
        roll = input("Roll: ")
        dept = input("Dept: ")
        f = open("students.txt", "a")
        f.write(name + "," + roll + "," + dept + "\n")
        f.close()
        print("Saved")

    elif c == "2":
        try:
            f = open("students.txt", "r")
            print(f.read())
            f.close()
        except:
            print("No records yet")

    elif c == "3":
        break
    else:
        print("Invalid choice")
