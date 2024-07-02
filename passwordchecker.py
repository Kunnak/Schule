import re

def is_valid_password():
    password = input("Passwort: ")
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[?.\-*!§$@´`%&[}+]).{8,}$"
    if re.match(pattern, password) is not None:
        print(f"Das Passwort ist gültig!")
    else:
        print(f"Das Passwort ist nicht gültig!")

is_valid_password()
