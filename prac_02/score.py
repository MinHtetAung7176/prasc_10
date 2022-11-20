def main():
    score = float(input("Enter score: "))
    determine_score(score)

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

