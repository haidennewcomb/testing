with open('test.txt', 'w') as f: 
   f.write('Hello')
   
with open('test.txt', 'a') as f2: 
   f2.write('\nHow are you?')

with open('test.txt', 'r') as file:
    line1 = file.readline()
    line2 = file.readline()
    print(f"Line 1: {line1.strip()}")
    print(f"Line 2: {line2.strip()}")


with open('test.txt', 'r') as file:
    lines = file.readlines()
    print(f"Number of lines: {len(lines)}")
    for i, line in enumerate(lines):
        print(f"Line {i+1}: {line.strip()}")