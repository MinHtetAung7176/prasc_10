def main():
    password = get_password()

def get_password():
    password = input("Enter your Password: ")
    for i in password:
        print("*", end="")

main()