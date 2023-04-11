from cryptography.fernet import Fernet
import os
import shutil


def write_key():
    if os.path.isfile("../MiscFiles/key.key") is False:
        written_key = Fernet.generate_key()
    with open("../MiscFiles/key.key", "wb") as key_file:
        # noinspection PyUnboundLocalVariable
        key_file.write(written_key)


def load_key():
    if os.path.isfile("../MiscFiles/key.key") is False:
        write_key()
    file = open("../MiscFiles/key.key", "rb")
    loaded_key = file.read()
    file.close()
    return loaded_key


def option_view():
    with open("../MiscFiles/passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            # noinspection SpellCheckingInspection
            user, passw = data.split("|")
            print(f"Username: {user} | Password:", fer.decrypt(passw.encode()).decode())


def option_add():
    username = input("Account username: ")
    pwd = input("Account password: ")

    with open("../MiscFiles/passwords.txt", "a") as f:
        f.write(username + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


key = load_key()
fer = Fernet(key)

while True:
    mode = input("Would you like to 'add' a new password, or 'view' stored passwords? Press 'Q' to quit...\n").lower()
    if mode == "q":
        break

    if mode == "add":
        option_add()
    elif mode == "view":
        option_view()
    else:
        print("No such option exists...")
        continue
