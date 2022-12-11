class my_dictionary(dict):

    def __init__(self):
        self = dict
    def add(self,key,value):
        self[key] = value

username_and_email = my_dictionary()
user_email = input("Email: ")
while user_email != "":
    while "@" in user_email:
        name = str(user_email.rstrip('@.edu.com.au.jcu.gmail.hostmail'))
        name = name.split(".")
        user_name = ' '.join(map(str,name)).title()
        decision = input(f"Is your name {user_name}? (Y/n)").upper()
        if decision == "NO" and decision == "N":
            user_name = input("Name: ").title()
        username_and_email.key = user_email
        username_and_email.value = user_name
        username_and_email.add(username_and_email.key , username_and_email.value)
        user_email = input("Email: ")

for i in username_and_email:
    print(f"{username_and_email.value} ({username_and_email.key})")
            
    

