# Assume 'colors.txt' contains: "Red\nGreen\nBlue"
with open('colors.txt', 'w') as file:
    file.write("Red\nGreen\nBlue")

with open('colors.txt', 'r') as file:
    lines = file.readlines()
    for line in reversed(lines): print(line.strip())
print(lines[1].strip())
print(len(lines))