import os
import pyttsx3

def engine(word):
    engine = pyttsx3.init()
    engine.say(word)
    engine.runAndWait()

def main_():
    print("")
    search = input("Search: ")

    print("Searching " + search)
    engine("Searching " + search)
    link = "https://www.google.com/search?q="+search
    os.startfile(link)

for x in range(100):
    main_()