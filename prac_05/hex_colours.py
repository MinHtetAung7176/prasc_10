CODE_TO_COLOR = {"Amber": "#ffbf00", "Aqua": "#00ffff", "Army Green": "#4b5320", "Ash Grey": "#b2beb5",
                 "Baby Blue": "#89cff0",
                 "Black": "#000000", "Brown": "#a52a2a", "Bronze": "#cd7f32",
                 "Jade": "#00a86b", "Red1": "#ff0000"}
color_name = input("Enter Colour Name: ").title()
while color_name != "":
    try:
        print(color_name, "is", CODE_TO_COLOR[color_name])
    except KeyError:
        print("Invalid Colour Name.")
    color_name = input("Enter Colour Name: ").title()
