import tkinter as tk
import math as m

get_font = open("customize/costumfont.fnt").read()

def addtion():
    entry1 = float(entrytext1.get())
    entry2 = float(entrytext2.get())
    entry3 = float(entrytext3.get())
    entry4 = float(entrytext4.get())
    calc = str(entry1+entry2+entry3+entry4)

    label['text'] = calc

def subtraction():
    entry1 = float(entrytext1.get())
    entry2 = float(entrytext2.get())
    entry3 = float(entrytext3.get())
    entry4 = float(entrytext4.get())
    calc = str(entry1-entry2-entry3-entry4)

    label['text'] = calc

def multiplication():
    entry1 = float(entrytext1.get())
    entry2 = float(entrytext2.get())
    entry3 = float(entrytext3.get())
    entry4 = float(entrytext4.get())
    calc = str(entry1*entry2*entry3*entry4)

    label['text'] = calc

def division():
    entry1 = float(entrytext1.get())
    entry2 = float(entrytext2.get())
    entry3 = float(entrytext3.get())
    entry4 = float(entrytext4.get())
    calc = str(entry1/entry2/entry3/entry4)

    label['text'] = calc

def square():
    entry1 = float(entrytext1.get())
    entry2 = float(entrytext2.get())
    entry3 = float(entrytext3.get())
    entry4 = float(entrytext4.get())
    calc = str(pow(entry1+entry2, entry3+entry4))

    label['text'] = calc

def square_root():
    entry1 = float(entrytext1.get())
    entry2 = float(entrytext2.get())
    entry3 = float(entrytext3.get())
    entry4 = float(entrytext4.get())
    calc = str(m.sqrt(entry1+entry2+entry3+entry4))

    label['text'] = calc

    label['text'] = calc

def perimeter():
    entry1 = float(entrytext1.get())
    entry2 = float(entrytext2.get())
    entry3 = float(entrytext3.get())
    entry4 = float(entrytext4.get())
    calc = str(entry1+entry2+entry3++entry4)

    label['text'] = calc

def area():
    entry1 = float(entrytext1.get())
    entry2 = float(entrytext2.get())
    calc = str(entry1*entry2)

    label['text'] = calc + " sq. km"

def percentage():
    entry1 = float(entrytext1.get())
    entry2 = float(entrytext2.get())
    entry3 = float(entrytext3.get())
    entry4 = float(entrytext4.get())
    comb_no = float(entry1+entry2+entry3)
    calc = comb_no/100*entry4

    label['text'] = calc

root = tk.Tk()
root.geometry("500x500")
root.maxsize(5000, 1000)
root.title("Calculator")

label = tk.Label(root, text="Answer will be displayed here", font=("Segoe UI", 20))
label.pack()

entrytext1 = tk.StringVar()
entryfield1 = tk.Entry(root, font=(get_font, 11), textvariable=entrytext1)
entryfield1.pack()

label2 = tk.Label(root, text=None, font=(get_font, 11))
label2.pack()

entrytext2 = tk.StringVar()
entryfield2 = tk.Entry(root, font=(get_font, 11), textvariable=entrytext2)
entryfield2.pack()

label3 = tk.Label(root, text=None, font=(get_font, 11))
label3.pack()

entrytext3 = tk.StringVar()
entryfield3 = tk.Entry(root, font=(get_font, 11), textvariable=entrytext3)
entryfield3.pack()

label4 = tk.Label(root, text=None, font=(get_font, 11))
label4.pack()

entrytext4 = tk.StringVar()
entryfield4 = tk.Entry(root, font=(get_font, 11), textvariable=entrytext4)
entryfield4.pack()

label5 = tk.Label(root, text=None, font=(get_font, 11))
label5.pack()

button1 = tk.Button(root, text="Add", font=(get_font, 11), command=addtion)
button1.pack()

button2 = tk.Button(root, text="Subtract", font=(get_font, 11), command=subtraction)
button2.pack()

button3 = tk.Button(root, text="Multiply", font=(get_font, 11), command=multiplication)
button3.pack()

button4 = tk.Button(root, text="Divide", font=(get_font, 11), command=division)
button4.pack()

button5 = tk.Button(root, text="Square", font=(get_font, 11), command=square)
button5.pack()

button6 = tk.Button(root, text="Square Root", font=(get_font, 11), command=square_root)
button6.pack()

button7 = tk.Button(root, text="Perimeter", font=(get_font, 11), command=perimeter)
button7.pack()

button8 = tk.Button(root, text="Area", font=(get_font, 11), command=area)
button8.pack()

button9 = tk.Button(root, text="Percentage", font=(get_font, 11), command=percentage)
button9.pack()

root.mainloop()