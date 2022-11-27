"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))

        # TODO: this line
        if result.isdigit():
            is_finished = True

    except:  # TODO - add the exception you want to catch after except
        print("The Value is not valid")
        is_finished = False

print("Valid result is:", result)