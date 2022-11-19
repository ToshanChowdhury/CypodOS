import os

username_import = open("account_login_details/username.user").read()
password_import = open("account_login_details/password.pass").read()
name_import = open("account_login_details/name.nme").read()
cde_import = open("account_login_details/secure_code.cde").read()

askusername = input("What is your username?: ")

if askusername == username_import:
    password = input("Welcome, " + name_import + " what is your password?: ")

    if password == password_import:
        security_code = input("What is your security code?: ")

        if security_code == cde_import:
            os.startfile("main.py")
        else:
            exit()
    else:
        exit()
else:
    exit()