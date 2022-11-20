def main():
    MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit """
    print(MENU)
    choice = input(">>> ").upper()
    get_valid_choice(choice, MENU)


def get_valid_choice(choice, MENU):
    while choice != "Q":
        if choice == "G":
            score = int(input("Enter Score: "))
            get_valid_score(score)
        elif choice == "P":
            determine_score(score)
        elif choice == "S":
            display_stars(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def display_stars(score):
    for i in range(0, score):
        print("*", end="")
    print()


def get_valid_score(score):
    while score < 0 or score > 100:
        print("Invalid Score")
        score = input("Enter Score: ")
    return score


def determine_score(score):
    if score < 0:
        print("Invalid score")
    else:
        if score > 100:
            print("Invalid score")
        elif score > 90:
            print("Excellent")
        elif score > 50:
            print("Passable")
        else:
            print("Bad")


main()
