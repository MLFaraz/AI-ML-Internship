class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
        self.issued = 0

    def available(self):
        return self.copies - self.issued

class Library:
    def __init__(self):
        self.books = []
        self.load()

    def load(self):
        try:
            f = open("books.txt", "r")
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    b = Book(parts[0], parts[1], int(parts[2]))
                    b.issued = int(parts[3])
                    self.books.append(b)
            f.close()
        except:
            pass

    def save(self):
        f = open("books.txt", "w")
        for b in self.books:
            f.write(b.title + "," + b.author + "," + str(b.copies) + "," + str(b.issued) + "\n")
        f.close()

    def add(self):
        t = input("Title: ")
        a = input("Author: ")
        c = input("Copies: ")
        try:
            c = int(c)
            self.books.append(Book(t, a, c))
            self.save()
            print("Book added")
        except:
            print("Invalid copies")

    def view(self):
        if not self.books:
            print("No books")
            return
        for b in self.books:
            print(b.title, "-", b.author, "- Available:", b.available(), "- Issued:", b.issued)

    def search(self):
        t = input("Enter title: ").lower()
        found = False
        for b in self.books:
            if t in b.title.lower():
                print(b.title, "-", b.author, "- Available:", b.available())
                found = True
        if not found:
            print("Not found")

    def issue(self):
        t = input("Title to issue: ").lower()
        for b in self.books:
            if t == b.title.lower():
                if b.available() > 0:
                    b.issued += 1
                    self.save()
                    print("Issued")
                else:
                    print("No copies left")
                return
        print("Book not found")

    def return_book(self):
        t = input("Title to return: ").lower()
        for b in self.books:
            if t == b.title.lower():
                if b.issued > 0:
                    b.issued -= 1
                    self.save()
                    print("Returned")
                else:
                    print("No issued copies")
                return
        print("Book not found")

lib = Library()
while True:
    print("\n1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")
    c = input("Choice: ")

    if c == "1":
        lib.add()
    elif c == "2":
        lib.view()
    elif c == "3":
        lib.search()
    elif c == "4":
        lib.issue()
    elif c == "5":
        lib.return_book()
    elif c == "6":
        break
    else:
        print("Invalid choice")
