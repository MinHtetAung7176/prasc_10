numbers = [3, 1, 4, 1, 5, 9, 2]
i = 5
g = 7
j = "3"
print(numbers[0])
print(numbers[-1])
print(numbers[3])
print(numbers[:-1])
print(numbers[3:4])
if i in numbers:
    print("5 in numbers")
if g in numbers:
    print("7 in numbers")
if j in numbers:
    print("3 in numbers")
numbers.append([6, 5, 3])
print(numbers)
numbers[0] = "ten"
print(numbers)
numbers[-1] = 1
print(numbers)
print(numbers[2:-1])
if 9 in numbers:
    print("9 is in numbers.")