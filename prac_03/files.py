OUT_FILE = "name.txt"
IN_FILE = "name.txt"
NUMBER_FILE = "number.txt"
out_file = open(OUT_FILE, 'w')
name = input("Enter your name: ")
out_file.write(name)
out_file.close()
in_file = open(IN_FILE, 'r')
lines = in_file.readlines()
print(lines)
num_file = open(NUMBER_FILE, 'r')
number = num_file.readlines()
for num_line in number:
    print(num_line.strip())
