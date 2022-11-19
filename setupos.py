import random
import os

codes = "40.92645", "16.2613", "18.9283", "99.26313", "80.27336", "100.9827", "92.735183", "86.92634", "90.26341", "67.92635", "17.6253", "15.35472", "16.2435", "18.17352", "902.2624"

print("CYPOD OS (Setup)")
print()
print("Welcome to setup CypodOS, your new strong powered operating system")
print()
name_get = input("What is your name?: ")
print()
username_get = input("What would you like to set your username as?: ")
print()
password_get = input("What would you like to set your password as?: ")
print()
birthdate_get = input("What is your birth date? (D/M/Y): ")
print()
code = random.choice(codes)

with open("account_login_details/name.nme", "w") as f:
    f.write(name_get)

with open("account_login_details/username.user", "w") as f:
    f.write(username_get)

with open("account_login_details/password.pass", "w") as f:
    f.write(password_get)

with open("account_login_details/birthdate.birth", "w") as f:
    f.write(birthdate_get)

with open("account_login_details/secure_code.cde", "w") as f:
    f.write(code)

print("Your security code is: " + code)
input("Copy your code.")
print()
print("Thank you for registering an account before using CypodOS.")
os.startfile("loginsystem.py")
exit()