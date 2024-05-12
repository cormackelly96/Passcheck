import re


def checkPassword():
    # Takes user input for their password
    password = input("Enter your password: ")
    # Checks if the users password meets the conditions
    test = re.match(r"[A-Za-z0-9@#$%^&+=]{8,}", password)

    while (
        test == None
    ):  # while the password is not a match. The user has to enter another password and the password is checked again.
        print(
            "That is a bad password. Please enter a password that is 8 characters long"
        )
        password = input("Enter your password: ")
        test = re.match(r"[A-Za-z0-9@#$%^&+=]{8,}", password)

    print("Your password is good!")


checkPassword()
