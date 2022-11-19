import os
import pyttsx3
import tkinter as tk

audio_speakers = pyttsx3.init()

def search():
    text = entrytextdata.get()
    format_text = "Searching, " + text + "..."
    label2['text'] = format_text
    audio_speakers.say("Searching, " + text + "...")
    audio_speakers.runAndWait()
    link = "https://www.google.com/search?q="+text
    os.startfile(link)

get_font = open("customize/costumfont.fnt").read()

window = tk.Tk()
window.title("Assistant")

label = tk.Label(window, text="Assistant", font=(get_font, 20))
label.pack()

label2 = tk.Label(text="", font=(get_font, 11))
label2.pack()

entrytextdata = tk.StringVar()
entrytext = tk.Entry(window, font=(get_font, 11), textvariable=entrytextdata)
entrytext.pack()

give_command = tk.Button(window, text="Submit Command", font=(get_font, 11), command=search)
give_command.pack()

window.geometry("500x500")
window.maxsize(500, 500)
window.mainloop()