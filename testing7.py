try:
    with open('nonexistent.txt', 'r') as file:
        content = file.read()
    print("File read successfully")
except FileNotFoundError:
    print("File not found")
print("Program continues")