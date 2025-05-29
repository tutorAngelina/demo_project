name = input("Enter your name: ")
age = input("Enter your age: ")
password = input("Enter your password: ")

user_profile = {
    "name": name,
    "age": age,
    "password": password
}

print("Profile created!")
tries = 3
while tries > 0:
    confirm_password = input("Please confirm your password: ")
    if confirm_password == user_profile["password"]:
        print("Password confirmed")
        break
    else:
        tries -= 1
        if tries > 0:
            print(f"Incorrect password. You have {tries} tries left.")
        else:
            print("Password not accepted")
