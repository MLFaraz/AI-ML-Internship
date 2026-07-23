try:
    f = open("sample.txt", "r")
    print(f.read())
    f.close()
except:
    print("File not found")
