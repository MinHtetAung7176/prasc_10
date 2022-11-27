"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# 1. When will a ValueError occur?
"""Value Error occurs while a user type in a float or strings rather than an integer"""
# 2. When will a ZeroDivisionError occur?
"""A ZeroDivisionError occurs when a user type a 0 in the denominator"""
# 3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""To avoid the possibility of a ZeroDivisionError we can add a while loop to check the user input and if it is a 0 
we can let the user to re-enter the value"""
