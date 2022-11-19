import math
import os

print("Terminal")

def exec():
    print("")
    command = input("$ ")

    # MEST: MESSAGE
    if "mest ?" in command:
        print("Mest")
        print("mest is a default command made for the terminal to interact with what you are saying")
        print("For example: mest, hello will print out hello as the output")

    if "mest," in command:
        word = command.replace("mest, ", "")
        print(word)

    # VER: current version of terminal and CypodOS
    if "ver ?" in command:
        print("Ver")
        print("ver is a default command made for the terminal to interact by saying the current version of your Operating System")
        print("For example: ver, will print out the current version of your terminal and Operating System")
        print("ver, os will print out the current operating system")
        print("ver, tr will print out the terminal's current version.")

    if "ver," in command:
        print("Operating System: 1.0 (24/10/2022)")
        print("Terminal: 1.0 (25/10/2022)")

    if "ver, os" in command:
        print("Operating System: 1.0 (24/10/2022)")

    if "ver, tr" in command:
        print("Terminal: 1.0 (25/10/2022")

    # math = CALCULATIONS
    if "math ?" in command:
        print("Math")
        print("Math is a default command built into the terminal application. This function asks you two numbers and solves the addition, subtraction, multiplication, division, square and square root.")
        print("For Example:")
        print("Input (User): math,")
        print("""Output: Asks you two numbers""")
        print("Input: You write the two numbers")
        print("Output: Answer of Addtion, Subtraction, Multiplication, Division, Square and Square Root.")

    if "math," in command:
        x1 = int(input("1st Number: "))
        x2 = int(input("2nd Number: "))
        add = str(x1+x2)
        subtract = str(x1-x2)
        multiply = str(x1*x2)
        divide = str(x1/x2)
        sq = str(pow(x1, x2))
        sqrt = str(math.sqrt(x1))
        sqrt2 = str(math.sqrt(x2))
        print("")
        print("Addtion: "+add)
        print("Subtraction: "+subtract)
        print("Multiplication: "+multiply)
        print("Division: "+divide)
        print("Square: "+sq)
        print("Square Root: (1) "+sqrt+" (2) "+sqrt2)

    # ope = OPENING FILES
    if "ope ?" in command:
        print("Ope")
        print("Ope is a command which open's the file that you want it to open.")
        print("For example: ope, example.txt")
        print("It will open the file 'example.txt'")

    if "ope," in command:
        word = command.replace("ope, ", "")

        try:
            os.startfile(word)
        except Exception as e:
            print(e)

    # ser = SEARCHING SOMETHING ONLINE
    if "ser ?" in command:
        print("Ser")
        print("Ser is a command that searches anything you want to search online.")
        print("For example: ser, apple")
        print("It will search apple online")

    if "ser, " in command:
        key_word = command.replace("ser, ", "")
        link = "https://www.google.com/search?q="+key_word

        try:
            os.startfile(link)
        except Exception as e:
            print(e)

    # rd = READ A FILE
    if "rd ?" in command:
        print("Rd")
        print("Rd is a command that open's and read's the file ans print's whatever the file contains, NOTE: It cannot insert images.")
        print("For exmaple: rd, example.txt")
        print("It will print the data inside example.txt")

    if "rd," in command:
        path = command.replace("rd, ", "")

        try:
            with open(path, "r") as f:
                document = f.read()
            print(document)
        except Exception as e:
            print(e)

    # help = HELP
    if "help" in command:
        print("Write ? with a space after the following commands shown in the screen.")
        print("""
        mest
        ver
        math
        ope
        ser
        rd
        """)

while True:
    exec()