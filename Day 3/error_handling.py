try:
    f = open("missing.txt", "r")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("File does not exist")
except PermissionError:
    print("No permission to read file")
except Exception as e:
    print("Error:", e)
