lines = ["Apple\n", "Banana\n", "Cherry\n"]
with open('fruits.txt', 'w') as file:
    print(open('fruits.txt').read())
    file.writelines(lines)
    for i, line in enumerate(lines): file.write(f"{i+1}. {line}")
print(len(lines))